for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
        continue
    if n == 2:
        print(-1)
        continue    

    ans = [1, 2, 3]
    s = 6
    for i in range(3, n):
        ans.append(s)
        s += s
    print(*ans)