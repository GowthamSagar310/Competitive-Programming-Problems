for _ in range(int(input())):
    n = int(input())

    # if n is divisible by a1, a2, a3, a4 
    # where [a1, a2, a3, a4] are consecutive

    # in a window of size 4 on the number line 
    # there must be exactly 1 number that is divisible by 4
    # there must be exactly 1 number that is divisible by 3
    # there must be exactly 2 numbers that is divisible by 2
    # there must by exactly 4 numbers that is divisible by 1

    # so, if there is 1 number which is divisible by 4
    # that means 4 divides n

    # say [14, 15, 16, 17] is the largest sequence for "n" 
    # size = 4
    # 16 is divisible by 4 (4)
    # 15 is divisible by 3 (3)
    # 14 is divisible by 3 (2)
    # everything is divisible by (1)
    # [1, 2, 3, 4] also divides "n"

    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
        else:
            break
    print(count)
