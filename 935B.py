n = int(input())
s = input()
x, y = 0, 0
coins = 0
for i in range(n):
    l = s[i]
    if i > 0 and y == x and s[i-1] == s[i]:
            coins += 1
    if l == 'U':
        y += 1
    else:
        x += 1
print(coins)