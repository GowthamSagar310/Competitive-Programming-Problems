for _ in range(int(input())):
    s = input()
    ans = s[0]
    i = 0
    while i < len(s):
        if s[i-1] == " ":
            ans += s[i]
        i += 1
    print(ans)