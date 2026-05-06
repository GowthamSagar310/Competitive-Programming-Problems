def get_ops(mid, a, b):
    if mid == 1: return float("inf")
    ops = mid-b
    while a:
        a //= b
        ops += 1
    return ops


for _ in range(int(input())):
    a, b = map(int, input().split())
    if a < b:
        print(0)
    elif a == b:
        print(2)
    else:
        
        # if b == 1, we cannot reduce a, so b += 1, ops = 1
        # if b == 2, this is going to take the maximum divisions
        # O(loga base 2)
        # max number = 10**9 = O(log 10** 9) ~= log (2 ** 30)
        # max number =~ 30 divisions are enough. 
        # b > 2, is always going take less the 30 divisons

        