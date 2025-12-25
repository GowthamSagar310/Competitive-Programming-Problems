for _ in range(int(input())):
    n = int(input())
    first_row = input()
    nth_row = input()
    count = 0
    updated = [False] * n
    for i in range(n):
        if nth_row[i] == "0": continue
        if first_row[i] == "0":
            count += 1
        elif i-1 >= 0 and first_row[i-1] == "1" and not updated[i-1]:
            count += 1
            updated[i-1] = True
        elif i+1 < n and first_row[i+1] == "1" and not updated[i+1]:
            count += 1
            updated[i+1] = True
    print(count)