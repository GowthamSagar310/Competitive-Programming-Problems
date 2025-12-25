for _ in range(int(input())):
    s = input()
    c = "codeforces"
    print(sum(1 if s[i] != c[i] else 0 for i in range(10)))