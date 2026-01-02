s = input()
ones = zeroes = 0
flag = False
for l in s:
    if l == "0":
        zeroes += 1
        ones = 0
    else:
        ones += 1
        zeroes = 0
    if ones == 7 or zeroes == 7:
        flag = True
        break
print("YES" if flag else "NO")