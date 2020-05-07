from urllib.request import urlopen
import time
import fc as Case0
import mcv_fc as Case1
import dh_fc as Case2
import lcv_fc as Case3
import mcv_dh_fc as Case4
import mcv_lcv_fc as Case5
import dh_lcv_fc as Case6
import mcv_dh_lcv_fc as Case7

#link = "http://magictour.free.fr/top1465"
#f = urlopen(link)
f = open("source.txt", "r")
n = 10 # change number of test cases here, max = 1465

algo0 = "0.fc            : "
algo1 = "1.mcv           : "
algo2 = "2.dh            : "
algo3 = "3.lcv           : "
algo4 = "4.mcv + dh      : "
algo5 = "5.mcv + lcv     : "
algo6 = "6.dh + lcv      : "
algo7 = "7.mcv + dh + lcv: "

avg_time_0 = 0
avg_time_1 = 0
avg_time_2 = 0
avg_time_3 = 0
avg_time_4 = 0
avg_time_5 = 0
avg_time_6 = 0
avg_time_7 = 0

avg_trial_0 = 0
avg_trial_1 = 0
avg_trial_2 = 0
avg_trial_3 = 0
avg_trial_4 = 0
avg_trial_5 = 0
avg_trial_6 = 0
avg_trial_7 = 0

num_fail_0 = 0
num_fail_1 = 0
num_fail_2 = 0
num_fail_3 = 0
num_fail_4 = 0
num_fail_5 = 0
num_fail_6 = 0
num_fail_7 = 0

result_file = open("new_result.txt", "w")

for id in range(1, n + 1):
    result_file.write("===== Sudoku " + str(id) + " =====\n" )
    line = f.readline()
    print(line)
    puzzle = [[0 for i in range(9)] for j in range(9)]
    for i in range(9):
        for j in range(9):
            number = line[9 * i + j]
            if number == '.':
                puzzle[i][j] = 0
            else:
                puzzle[i][j] = int(number)

    # fc only
    print("start fc")
    solved0 = True
    sudoku0 = Case0.Sudoku(puzzle)
    start0 = time.time()
    try:
        ans0 = sudoku0.solve()
    except:
        num_fail_0 += 1
        solved0 = False
    finally:
        if solved0:
            end0 = time.time()
            time0 = end0 - start0
            trial0 = sudoku0.number_of_tries
            avg_time_0 += time0
            avg_trial_0 += trial0
            result_file.write(algo0 + "time:%.5f   trial:%d\n" % (time0, trial0))
        else:
            result_file.write(algo0 + "Fail!\n")

    # mcv
    print("start mcv")
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
            result_file.write(algo1 + "time:%.5f   trial:%d\n" % (time1, trial1))
        else:
            result_file.write(algo1 + "Fail!\n")

    # dh
    print("start dh")
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
            result_file.write(algo2 + "time:%.5f   trial:%d\n" % (time2, trial2))
        else:
            result_file.write(algo2 + "Fail!\n")

    # lcv
    print("start lcv")
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
            result_file.write(algo3 + "time:%.5f   trial:%d\n" % (time3, trial3))
        else:
            result_file.write(algo3 + "Fail!\n")

    # mcv + dh
    print("start mcv + dh")
    solved4 = True
    sudoku4 = Case4.Sudoku(puzzle)
    start4 = time.time()
    try:
        ans4 = sudoku4.solve()
    except:
        num_fail_4 += 1
        solved4 = False
    finally:
        if solved4:
            end4 = time.time()
            time4 = end4 - start4
            trial4 = sudoku4.number_of_tries
            avg_time_4 += time4
            avg_trial_4 += trial4
            result_file.write(algo4 + "time:%.5f   trial:%d\n" % (time4, trial4))
        else:
            result_file.write(algo4 + "Fail!\n")

    # mcv + lcv
    print("start mcv + lcv")
    solved5 = True
    sudoku5 = Case5.Sudoku(puzzle)
    start5 = time.time()
    try:
        ans5 = sudoku5.solve()
    except:
        num_fail_5 += 1
        solved5 = False
    finally:
        if solved5:
            end5 = time.time()
            time5 = end5 - start5
            trial5 = sudoku5.number_of_tries
            avg_time_5 += time5
            avg_trial_5 += trial5
            result_file.write(algo5 + "time:%.5f   trial:%d\n" % (time5, trial5))
        else:
            result_file.write(algo5 + "Fail!\n")

    # dh + lcv
    print("start dh + lcv")
    solved6 = True
    sudoku6 = Case6.Sudoku(puzzle)
    start6 = time.time()
    try:
        ans6 = sudoku6.solve()
    except:
        num_fail_6 += 1
        solved6 = False
    finally:
        if solved6:
            end6 = time.time()
            time6 = end6 - start6
            trial6 = sudoku6.number_of_tries
            avg_time_6 += time6
            avg_trial_6 += trial6
            result_file.write(algo6 + "time:%.5f   trial:%d\n" % (time6, trial6))
        else:
            result_file.write(algo6 + "Fail!\n")

    # mcv + dh + lcv
    print("start mcv + dh + lcv")
    solved7 = True
    sudoku7 = Case7.Sudoku(puzzle)
    start7 = time.time()
    try:
        ans7 = sudoku7.solve()
    except:
        num_fail_7 += 1
        solved7 = False
    finally:
        if solved7:
            end7 = time.time()
            time7 = end7 - start7
            trial7 = sudoku7.number_of_tries
            avg_time_7 += time7
            avg_trial_7 += trial7
            result_file.write(algo7 + "time:%.5f   trial:%d\n" % (time7, trial7))
        else:
            result_file.write(algo7 + "Fail!\n")

result_file.write("===== Final Result =====\n")
result_file.write("===> Total number of failed puzzle:\n")
result_file.write(algo0 + "%d\n" % (num_fail_0))
result_file.write(algo1 + "%d\n" % (num_fail_1))
result_file.write(algo2 + "%d\n" % (num_fail_2))
result_file.write(algo3 + "%d\n" % (num_fail_3))
result_file.write(algo4 + "%d\n" % (num_fail_4))
result_file.write(algo5 + "%d\n" % (num_fail_5))
result_file.write(algo6 + "%d\n" % (num_fail_6))
result_file.write(algo7 + "%d\n" % (num_fail_7))

result_file.write("===> Average solving time:\n")
avg_time_0 /= (n - num_fail_0)
avg_time_1 /= (n - num_fail_1)
avg_time_2 /= (n - num_fail_2)
avg_time_3 /= (n - num_fail_3)
avg_time_4 /= (n - num_fail_4)
avg_time_5 /= (n - num_fail_5)
avg_time_6 /= (n - num_fail_6)
avg_time_7 /= (n - num_fail_7)
result_file.write(algo0 + "%.5f\n" % (avg_time_0))
result_file.write(algo1 + "%.5f\n" % (avg_time_1))
result_file.write(algo2 + "%.5f\n" % (avg_time_2))
result_file.write(algo3 + "%.5f\n" % (avg_time_3))
result_file.write(algo4 + "%.5f\n" % (avg_time_4))
result_file.write(algo5 + "%.5f\n" % (avg_time_5))
result_file.write(algo6 + "%.5f\n" % (avg_time_6))
result_file.write(algo7 + "%.5f\n" % (avg_time_7))

result_file.write("===> Average number of trials:\n")
avg_trial_0 /= (n - num_fail_0)
avg_trial_1 /= (n - num_fail_1)
avg_trial_2 /= (n - num_fail_2)
avg_trial_3 /= (n - num_fail_3)
avg_trial_4 /= (n - num_fail_4)
avg_trial_5 /= (n - num_fail_5)
avg_trial_6 /= (n - num_fail_6)
avg_trial_7 /= (n - num_fail_7)
result_file.write(algo0 + "%.5f\n" % (avg_trial_0))
result_file.write(algo1 + "%.5f\n" % (avg_trial_1))
result_file.write(algo2 + "%.5f\n" % (avg_trial_2))
result_file.write(algo3 + "%.5f\n" % (avg_trial_3))
result_file.write(algo4 + "%.5f\n" % (avg_trial_4))
result_file.write(algo5 + "%.5f\n" % (avg_trial_5))
result_file.write(algo6 + "%.5f\n" % (avg_trial_6))
result_file.write(algo7 + "%.5f\n" % (avg_trial_7))

result_file.close()
f.close()