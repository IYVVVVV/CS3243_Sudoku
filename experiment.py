from urllib.request import urlopen
import time
import mrv_lcv_fc as Case1
import mrv_dh_fc as Case2
import mrv_fc as Case3

link = "http://magictour.free.fr/top1465"
f = urlopen(link)
n = 100 # change number of test cases here, max = 1465

avg_time_1 = 0
avg_time_2 = 0
avg_time_3 = 0

avg_trial_1 = 0
avg_trial_2 = 0
avg_trial_3 = 0

num_fail_1 = 0
num_fail_2 = 0
num_fail_3 = 0

result_file = open("result.txt", "w")

for id in range(1, n + 1):
    result_file.write("===== Sudoku " + str(id) + " =====\n" )
    line = f.readline().decode()
    puzzle = [[0 for i in range(9)] for j in range(9)]
    for i in range(9):
        for j in range(9):
            number = line[9 * i + j]
            if number == '.':
                puzzle[i][j] = 0
            else:
                puzzle[i][j] = int(number)

    # mrv + lcv + fc
    solved1 = True
    sudoku1 = Case1.Sudoku(puzzle)
    start1 = time.time()
    try:
        ans1 = sudoku1.solve()
    except:
        num_fail_1 += 1
        solved1 = False
    finally:
        if solved1:
            end1 = time.time()
            time1 = end1 - start1
            trial1 = sudoku1.number_of_tries
            avg_time_1 += time1
            avg_trial_1 += trial1
            result_file.write("1.mrv+lcv+fc:   time:%.5f   trial:%d\n" % (time1, trial1))
        else:
            result_file.write("1.mrv+lcv+fc: Fail!\n")

    # mrv + dh + fc
    solved2 = True
    sudoku2 = Case2.Sudoku(puzzle)
    start2 = time.time()
    try:
        ans2 = sudoku2.solve()
    except:
        num_fail_2 += 1
        solved2 = False
    finally:
        if solved2:
            end2 = time.time()
            time2 = end2 - start2
            trial2 = sudoku2.number_of_tries
            avg_time_2 += time2
            avg_trial_2 += trial2
            result_file.write("2.mrv+dh+fc :   time:%.5f   trial:%d\n" % (time2, trial2))
        else:
            result_file.write("2.mrv+dh+fc : Fail!")

    # mrv + fc
    solved3 = True
    sudoku3 = Case3.Sudoku(puzzle)
    start3 = time.time()
    try:
        ans3 = sudoku3.solve()
    except:
        num_fail_3 += 1
        solved3 = False
    finally:
        if solved3:
            end3 = time.time()
            time3 = end3 - start3
            trial3 = sudoku3.number_of_tries
            avg_time_3 += time3
            avg_trial_3 += trial3
            result_file.write("3.mrv+fc    :   time:%.5f   trial:%d\n" % (time3, trial3))
        else:
            result_file.write("3.mrv+fc    : Fail!")

result_file.write("===== Final Result =====\n")
result_file.write("===> Total number of failed puzzle:\n")
result_file.write("1.mrv+lcv+fc: %d\n" % (num_fail_1))
result_file.write("2.mrv+dh+fc : %d\n" % (num_fail_2))
result_file.write("3.mrv+fc    : %d\n" % (num_fail_3))

result_file.write("===> Average solving time:\n")
avg_time_1 /= (n - num_fail_1)
avg_time_2 /= (n - num_fail_2)
avg_time_3 /= (n - num_fail_3)
result_file.write("1.mrv+lcv+fc: %.5f\n" % (avg_time_1))
result_file.write("2.mrv+dh+fc : %.5f\n" % (avg_time_2))
result_file.write("3.mrv+fc    : %.5f\n" % (avg_time_3))

result_file.write("===> Average number of trials:\n")
avg_trial_1 /= (n - num_fail_1)
avg_trial_2 /= (n - num_fail_2)
avg_trial_3 /= (n - num_fail_3)
result_file.write("1.mrv+lcv+fc: %.5f\n" % (avg_trial_1))
result_file.write("2.mrv+dh+fc : %.5f\n" % (avg_trial_2))
result_file.write("3.mrv+fc     : %.5f\n" % (avg_trial_3))

result_file.close()
