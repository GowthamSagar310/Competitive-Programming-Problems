from math import isqrt
def is_prime(x):
    if x == 1: return False
    if x == 2: return True
    if x % 2 == 0: return False
    for i in range(3, isqrt(x)+1, 2):
        if x % i == 0:
            return False
    return True

for _ in range(int(input())):
    x, k = map(int, input().split())
    if k == 1:
        print("YES" if is_prime(x) else "NO")
    else:
        if k == 2 and x == 1:
            print("YES")
        else:
            print("NO")