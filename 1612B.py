# def solve(n, a, b):
#     res = []
#     for i in range(1, n+1):
#         if i != a and i != b:
#             res.append(i)
    
#     if res:
#         # for second half
#         n1 = (n-2) // 2
#         maxi = res[n1-1]
#         if maxi > b: return [-1]

#         # for first half
#         mini = res[n1]
#         if mini < a: return [-1]
    
#     p1, p2 = 0, n-3
#     ans = [0] * n
#     ans[0] = a
#     ans[(n+1)//2] = b
#     i = 0
#     while i < n:
#         if ans[i] == 0:
#             if i < n//2:
#                 ans[i] = res[p2]
#                 p2 -= 1
#             else:
#                 ans[i] = res[p1]
#                 p1 += 1
#         i += 1
#     return ans

# SIMPLER solution
def solve(n, a, b):
    res = [a]
    for i in range(n, 0, -1):
        if i != a and i != b:
            res.append(i)
    res.append(b)
    if min(res[0:n//2]) == a and max(res[n//2:]) == b:
        return res
    else:
        return [-1]

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    arr = [0] * n
    
    # when is it not possible ? 
    # first_half -> a should be the minimum
    # meaning there should be (n//2)-1 elements which are more than "a", exlcuding nmbers in the second half

    # second_half -> b should be the maximum
    # meaning there should be (n//2)-1 elements which are less than "b", excluding numbers in the first half

    
    print(*solve(n, a, b))