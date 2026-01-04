from collections import Counter
import math

for _ in range(int(input())):
    n = int(input())
    arr = input().split() # converting map(int, input().split()) is useless here and causes TLE

    # 0 1 3 3 7 0
    # 
    # clone 1 + 2 ops: 0 1 3 3 7 0 == 3 3 3 3 7 0
    # clone 2 + 2 ops: 3 3 3 3 7 0 == 3 3 3 3 3 3
    # total ops = 1 + 2 + 1 + 2 = 6

    # most frequent number is choosen
    # and the number of available "most frequent number" increases

    # freqs = Counter(arr)
    # max_f = max(freqs.values())
    # ops = 0
    # while max_f < n:
    #     # clone the array
    #     ops += 1
    #     # swap elements
    #     items_to_swap = min(max_f, n-max_f)
    #     ops += items_to_swap
    #     # max_f increases by items_to_swap
    #     max_f += items_to_swap
    # print(ops)

    # mathematical solution
    # total number of swaps needed = n-max_f
    
    # upon each clone, the max_f capacity doubles
    # f -> 2f -> 4f -> 8f -> 2^k.f
    # how many ops ? k ops 
    # how many at the last = 2^k.f 
    # 2^k * f >= n
    # k = ceil(log2 (n/f))
    
    freqs = Counter(arr)
    max_f = max(freqs.values())
    k = math.ceil(math.log2(n/max_f))
    print(n-max_f+k)
