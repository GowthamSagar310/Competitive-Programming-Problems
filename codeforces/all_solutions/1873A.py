for _ in range(int(input())):
    s = input()
    diff = 0
    for i in range(3):
        if i != ord(s[i])-ord('a'):
            diff += 1
    if diff > 2:
        print("NO")
    else:
        print("YES")