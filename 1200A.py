n = int(input())
s = input()
ans = [0] * 10
max_l, min_r = 0, 9
for i in range(n):
    c = s[i]
    if c == "L":
        for j in range(10):
            if ans[j] == 0:
                if j == max_l: max_l += 1
                ans[j] = 1
                break
    elif c == "R":
        for j in range(9, -1, -1):
            if ans[j] == 0:
                if j == min_r: min_r -= 1
                ans[j] = 1
                break
    else:
        ans[int(c)] = 0
print("".join(map(str, ans)))