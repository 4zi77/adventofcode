import time
import statistics as st

test_dict = {
    "test_1" : [0,3,6],  # 436 175594
    "test_2" : [1,3,2],  # 1 2578
    "test_3" : [2,1,3],  # 10 3544142
    "test_4" : [1,2,3],  # 27 261214
    "test_5" : [2,3,1],  # 78 6895259
    "test_6" : [3,2,1],  # 438 18
    "test_7" : [3,1,2],  # 1836 362
}
real = [14,1,17,0,3,20]
iteration = 2020
iteration2 = 30000000

def predict_ith(L, it, it2):
    occurences = {}
    for i, v in enumerate(L):
        occurences[v] = i+1
    last_val = 0
    for i in range(len(L)+1, it2):
        if last_val in occurences:
            new_val = i - occurences[last_val]
            occurences[last_val] = i
        else:
            occurences[last_val] = i
            new_val = 0
        last_val = new_val
        # print(f"Dict at step {i} : {occurences}")
        if i == it-1:
            print(f"Value = {last_val}")
    return last_val

if __name__ == '__main__':
    times = []
    for i in range(1, 8):
        start = time.time()
        number_list = test_dict[f"test_{i}"]
        print(predict_ith(number_list, iteration, iteration2), '\n')
        times.append(time.time()-start)
    start = time.time()
    print(predict_ith(real, iteration, iteration2))
    times.append(time.time() - start)
    mini, maxi, avgt, stdt = min(times), max(times), st.mean(times), st.stdev(times)
    print(f"Times day15 part 2 : Min = {mini:2f}s, Max = {maxi:2f}s, Avg = {avgt:2f}s, Std = {stdt:2f}s")
