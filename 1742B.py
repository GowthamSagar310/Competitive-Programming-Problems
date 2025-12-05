for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print("YES" if len(set(arr)) == n else "NO")