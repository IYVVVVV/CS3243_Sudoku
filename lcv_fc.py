import sys
import copy
import math
import time
import random

# Running script: given code can be run with the command:
# python file.py, ./path/to/init_state.txt ./output/output.txt


class Sudoku(object):
    def __init__(self, puzzle):
        # you may add more attributes if you need
        self.puzzle = puzzle  # self.puzzle is a list of lists
        self.ans = copy.deepcopy(puzzle)  # self.ans is a list of lists
        self.number_of_tries = 0

    def solve(self):
        # TODO: Write your code here
        # Try to implement without any inference mechanism here.
        empty_grids = self.get_empty_grids()
        domains = self.get_all_domains(empty_grids, self.ans)

        self.ans = self.recursive_solve(
            empty_grids, self.ans, domains)

        # print(self.ans)
        return self.ans

    # Some helper functions are defined below.

    def recursive_solve(self, empty_grids, ans, domains):
        if (len(empty_grids) == 0):  # Finished solving
            return ans

        # Getting the next position, and its domain
        position, domain = self.get_next_var(
            empty_grids, ans, domains)

        # Filling up this position, so we are deleting it from domains and empty_grids
        del domains[position]
        empty_grids.remove(position)

        row = position[0]
        col = position[1]

        affected_pos = self.get_affected(domains, position)

        def constraining_num(value):
            decrease_num = 0
            for pos in affected_pos:
                if value in domains[pos]:
                    decrease_num += 1
            return decrease_num

        sortedDomain = sorted(domain, key=constraining_num)

        for val in sortedDomain:
            self.number_of_tries += 1
            # Getting the least constraining value
            ans[row][col] = val

            # Getting the new domain by constraint propagation (INFERENCE)
            newDomains, isFailure = self.get_new_domains(
                domains, affected_pos, position, val)

            if isFailure:
                continue

            newAns = self.recursive_solve(
                empty_grids, ans, newDomains)

            # This means that recursive_solve returns a valid answer
            if newAns is not None:
                return newAns

        # Domain size reduced to 0 before returning a valid ans, backtrack
        domains[position] = domain
        ans[row][col] = 0
        empty_grids.append(position)
        return None

    # Checking if 2 positions are 'related'
    def is_affected(self, pos1, pos2):
        return pos1[0] == pos2[0] or pos1[1] == pos2[1] or self.get_block_id(pos1[0], pos1[1]) == self.get_block_id(pos2[0], pos2[1])

    # From old domains and the changed value at a certain position, only check fix domain of positions that are affected
    def get_new_domains(self, old_domains, affected_pos, changed_pos, value):
        new_domains = {}
        for pos, domain in old_domains.items():
            domain_copy = domain
            if pos in affected_pos and value in domain:
                domain_copy = list(domain)
                domain_copy.remove(value)
                if len(domain_copy) == 0:
                    return {}, True
            new_domains[pos] = domain_copy
        return new_domains, False

    # Initial call to get all the domains
    def get_all_domains(self, empty_grids, ans):
        domains = {}
        for pos in empty_grids:
            domains[pos] = self.get_domain(pos[0], pos[1], ans)
        return domains

    # Get a list of affected position
    def get_affected(self, domains, changed_pos):
        affected_pos = []
        for pos in domains.keys():
            if self.is_affected(changed_pos, pos):
                affected_pos.append(pos)
        return set(affected_pos)

    # Can attempt to add more variable heuristics here
    def get_next_var(self, empty_grids, ans, domains):
        for pos, domain in domains.items():
            return pos, domain

    # Get all empty grid positions.
    # A position is stored in tuple (row, col).
    def get_empty_grids(self):
        empty_grids = []
        for i in range(9):
            for j in range(9):
                if self.ans[i][j] == 0:
                    empty_grids.append(tuple([i, j]))
        return empty_grids

    # Get a unit of 1 to 9.
    # Can use value ordering heuristics to change this method
    def get_unit(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(nums)
        return nums

    # Get all none-zero num in the same row.
    # row num can be 0 to 8.
    def get_row_nums(self, row, ans):
        row_nums = []
        for num in ans[row]:
            if num != 0:
                row_nums.append(num)
        return row_nums

    # Get all none-zero num in the same col.
    # col num can be 0 to 8.
    def get_col_nums(self, col, ans):
        col_nums = []
        for i in range(9):
            num = ans[i][col]
            if num != 0:
                col_nums.append(num)
        return col_nums

    # Get the block index for given row and col.
    # each block is a 3 * 3 grid.
    def get_block_id(self, row, col):
        row_id = int(math.ceil((row + 0.1) / 3))
        col_id = int(math.ceil((col + 0.1) / 3))
        block_id = 3 * (row_id - 1) + col_id
        return block_id

    # Get all non-zero num in the same block.
    # block_id can be 0 to 8.
    def get_block_nums(self, block_id, ans):
        block_nums = []
        row_end = int(math.ceil(block_id / 3) * 3)
        if block_id % 3 == 0:
            col_end = 9
        else:
            col_end = block_id % 3 * 3
        for i in range(row_end - 3, row_end):
            for j in range(col_end - 3, col_end):
                num = ans[i][j]
                if num != 0:
                    block_nums.append(num)
        return block_nums

    # Get domain for the grid in given row and col.
    def get_domain(self, row, col, ans):
        init_domain = self.get_unit()
        block_id = self.get_block_id(row, col)
        block_nums = self.get_block_nums(block_id, ans)
        row_nums = self.get_row_nums(row, ans)
        col_nums = self.get_col_nums(col, ans)
        unable_nums = list(set(block_nums + row_nums + col_nums))
        for num in unable_nums:
            if num in init_domain:
                init_domain.remove(num)
        return set(init_domain)

    # you may add more classes/functions if you think is useful
    # However, ensure all the classes/functions are in this file ONLY
    # Note that our evaluation scripts only call the solve method.
    # Any other methods that you write should be used within the solve() method.


if __name__ == "__main__":
    # STRICTLY do NOT modify the code in the main function here
    if len(sys.argv) != 3:
        print("\nUsage: python CS3243_P2_Sudoku_XX.py input.txt output.txt\n")
        raise ValueError("Wrong number of arguments!")

    try:
        f = open(sys.argv[1], 'r')
    except IOError:
        print("\nUsage: python CS3243_P2_Sudoku_XX.py input.txt output.txt\n")
        raise IOError("Input file not found!")

    puzzle = [[0 for i in range(9)] for j in range(9)]
    lines = f.readlines()

    i, j = 0, 0
    for line in lines:
        for number in line:
            if '0' <= number <= '9':
                puzzle[i][j] = int(number)
                j += 1
                if j == 9:
                    i += 1
                    j = 0

    sudoku = Sudoku(puzzle)
    ans = sudoku.solve()

    with open(sys.argv[2], 'a') as f:
        for i in range(9):
            for j in range(9):
                f.write(str(ans[i][j]) + " ")
            f.write("\n")
