# def solve(n, k1, k2, w, b):
#     # placing white 
#     w -= min(k1, k2)
#     if w > 0:
#         w -= abs(k1-k2) // 2
#         if w > 0:
#             return "NO"
    
#     # placing black
#     b1, b2 = n-k1, n-k2
#     b -= min(b1, b2)
#     if b > 0:
#         b -= abs(b1-b2) // 2
#         if b > 0:
#             return "NO"
#     return "YES"


for _ in range(int(input())):
    n, k1, k2 = map(int, input().split())
    w, b = map(int, input().split())
    # print(solve(n, k1, k2, w, b))

    if k1 + k2 >= 2 * w and (n - k1) + (n - k2) >= 2 * b:
        print("YES")
    else:
        print("NO")
