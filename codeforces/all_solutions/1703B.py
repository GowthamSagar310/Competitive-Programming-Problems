for _ in range(int(input())):
    n = int(input())
    s = input()
    seen = [False] * 26
    ballons = 0
    for l in s:
        index = ord(l)-ord('A')
        if seen[index]:
            ballons += 1
        else:
            ballons += 2
        seen[index] = True
    print(ballons) 