for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())
    if s < s[::-1]:
        print("YES")
    else:
        if len(set(s)) > 1 and k:
            print("YES")
        else:
            print("NO")

