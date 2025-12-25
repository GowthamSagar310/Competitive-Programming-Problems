n, k = map(int, input().split())

# i = 5
# count = 0
# while n and time_to_solve_p >= i:
#     count += 1
#     time_to_solve_p -= i 
#     i += 5
#     n -= 1
# print(count)

count = total = 0
for i in range(1, n+1):
    total += 5 * i
    if total <= 240-k:
        count += 1
    else:
        break
print(count)