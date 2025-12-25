for _ in range(int(input())):
    s = input()
    print("YES" if sum(map(int, list(s[:3]))) == sum(map(int, list(s[3:]))) else "NO")
    