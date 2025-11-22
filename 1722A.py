for _ in range(int(input())):
    n = int(input())
    s = input()
    if "".join(sorted(s)) == "Timru":
        print("YES")
    else:
        print("NO")