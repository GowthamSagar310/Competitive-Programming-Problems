n = int(input())
classes = []
for _ in range(n): classes.append(input())

maxi = 0
for i in range(7):
    count = 0
    for j in range(n):
        count += int(classes[j][i])
    maxi = max(maxi, count)
print(maxi)