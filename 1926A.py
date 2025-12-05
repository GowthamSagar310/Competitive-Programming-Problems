for _ in range(int(input())):
    s = input()
    a_count = s.count("A")
    b_count = 5 - a_count
    print("A" if a_count > b_count else "B")