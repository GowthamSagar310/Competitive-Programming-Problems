# def alternating_seq(i, n):
#     end = i+1
#     while end < n:
#         if s[end] == s[end-1]:
#             break
#         end += 1
#     return end

# def solve(s):
#     n = len(s)
#     k = 1
#     i = 1
#     while i < n:
#         if s[i] == s[i-1]:
#             if k:
#                 end = alternating_seq(i, n)
#                 k -= 1
#                 i = end
#             else:
#                 return False
#         i += 1
#     return True

def solve(s):
    n = len(s)
    ans = 0
    for i in range(1, n):
        ans += s[i] == s[i-1]
    return ans <= 2

for _ in range(int(input())):
    s = input()
    print("YES" if solve(s) else "NO")