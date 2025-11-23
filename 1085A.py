e = input()
n = len(e)

# if n & 1, start from left 
# else, start from right

left = True if n & 1 else False
l, r = 0, n-1
res = []
for _ in range(n):
    if left:
        res.append(e[l])
        l += 1
    else:
        res.append(e[r])
        r -= 1
    left = not left
print("".join(reversed(res)))