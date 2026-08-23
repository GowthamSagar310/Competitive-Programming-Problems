for _ in range(int(input())):
    n = int(input())
    s = input()
    s_sorted = "".join(sorted(s))

    if s == s_sorted:
        print(0)
        continue

    ans = [i+1 for i in range(n) if s[i] != s_sorted[i]]
    print(1)
    print(len(ans), *ans)
    