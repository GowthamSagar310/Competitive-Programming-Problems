for _ in range(int(input())):
    n = int(input())
    s = input()
    if int(s[0]) < int(s[1:]):
        print("YES")
        print(2)
        print(f"{s[0]} {s[1:]}")
    else:
        print("NO")
