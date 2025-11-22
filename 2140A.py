for _ in range(int(input())):
    n = int(input())
    s = input()
    zero_count = s.count("0")
    one_count = n-zero_count
    print(s[:zero_count].count("1"))