for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    s = set(arr)
    while len(s) not in s:
        s.add(len(s))
    print(len(s))