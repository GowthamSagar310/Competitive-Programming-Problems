x = int(input())

# 1 <= a, b <= x
# a % b == 0
# a * b > x
# a / b < x

# what if a = 2b ? 

# x = 17
# x, x//2

if x == 1:
    print(-1)
else:
    print(x-(x%2), end = ' ')
    print(2)