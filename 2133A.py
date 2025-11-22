for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print("YES" if n-len(set(arr)) > 0 else "NO")