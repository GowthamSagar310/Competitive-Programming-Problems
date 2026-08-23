def is_fair(n):
    temp = n
    while temp:
        d = temp % 10
        if d != 0:
            if n % d != 0:
                return False
        temp //= 10
    return True
for _ in range(int(input())):
    n = int(input())
    while True:
        if is_fair(n):
            print(n)
            break
        n += 1

# we can brute force because the number is not far away
# if the number has to be divisible by 1-9, then
# it must be divisible by LCM(1...9)
# so, the nearest multiple of 2520 should be that far away from the n
