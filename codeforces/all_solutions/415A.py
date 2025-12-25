n, m = map(int, input().split())
arr = list(map(int, input().split()))
# ans = [-1] * n
# for button in arr:
#     for i in range(button-1, n):
#         if ans[i] == -1:
#             ans[i] = button
#         else:
#             break
# print(" ".join(map(str, ans)))

# this problem can be solved in reverse too. 
# for each bulb, see which button turns it off first.

ans = [-1] * n
for i in range(n):
    bulb = i+1
    for button in arr:
        if bulb >= button:
            ans[i] = button
            break
print(" ".join(map(str, ans)))