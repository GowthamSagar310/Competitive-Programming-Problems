for _ in range(int(input())):
    n = int(input())
    s, t = input().split()
    print("YES" if sorted(s) == sorted(t) else "NO")
