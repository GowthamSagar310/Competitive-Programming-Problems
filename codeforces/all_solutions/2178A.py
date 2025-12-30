for _ in range(int(input())):
    s = input()
    y_count = s.count("Y")
    n_count = len(s) - y_count
    print("YES" if y_count <= n_count else "NO")
