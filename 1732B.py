for _ in range(int(input())):
    n = int(input())
    s = input()
    ops = 0
    for i in range(1, n):
        current_val = 1-int(s[i]) if ops & 1 else int(s[i])
        prev_val = 1-int(s[i-1]) if ops & 1 else int(s[i-1])
        if current_val == 0 and prev_val == 1:
            ops += 1
    print(ops)