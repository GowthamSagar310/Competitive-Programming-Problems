from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    # to maximize alice's score, 
    # 1. collect all numbers with freq = 1
    # 2. freq numbers with freq > 1, Bob can always choose what alice is choosing,
    #    so alice never get that extra point for getting all. 

    freq = Counter(arr)
    # alice = True
    # points = 0
    # for k, v in freq.items():
    #     if v > 1:
    #         points += 1
    #     else:
    #         points += 2 if alice else 0
    #         alice = not alice
    # print(points)

    exactly_one = more_than_one = 0
    for v in freq.values():
        if v > 1: more_than_one += 1
        else: exactly_one += 1
    
    print(2 * ((exactly_one+1)//2) + more_than_one)