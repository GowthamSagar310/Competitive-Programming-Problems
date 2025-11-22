import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    # all the numbers < k should be present 
    # if there is k in arr, that needs to be replaced

    # k = 2
    # 2 5 5 5 5

    # we have to replace the 2 
    # we have to also make sure 0, 1 are present
    # max(2's count, < k values count)
    # max(1, 2)
    # ops = 2
    

    # k = 2
    # 2 2 2 0 1
    # max(2's count, < k values count)
    # max(3, 0)
    # ops = 3

    k_count = 0
    less_than_k = [False] * k
    for val in arr:
        if val == k:
            k_count += 1
        if val < k:
            less_than_k[val] = True
    
    missing = k - sum(less_than_k)
    print(max(k_count, missing))
