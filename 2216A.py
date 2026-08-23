from collections import defaultdict
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split())) # limits
    b = list(map(int, input().split())) # initial
    indices = defaultdict(list)
    s = 0
    ops_req = 0
    for i, val in enumerate(b):
        if val != k+1:
            indices[val].append(i+1)
            s += val
            ops_req += (k+1)-val
    if ops_req == 0:
        print(0)
        print()
    elif ops_req > 1000:
        print(-1)
    else:
        print(ops_req)
        ans = []
        for i in range(k, 0, -1):
            for idx in indices[i]:
                ans.extend([idx] * (k+1-i))
        print(*ans)

        # check_ops = 0
        # for index in ans:
        #     b[index-1] += 1
        #     check_ops += 1
        # print(b, check_ops)
