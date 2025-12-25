for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == b: print(0)
    elif a % b == 0 or b % a == 0: print(1)
    else: print(2)