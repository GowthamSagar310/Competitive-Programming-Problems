for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if a == b:
        print(0)
        continue

    if sum(a) == 0:
        print(-1)
        continue

    if sum(b) == n:
        print(-1)
        continue

    ones = sum([a[i] == 1 and a[i] != b[i] for i in range(n)])
    if ones & 1:
        print(1)
    else:
        print(2)
