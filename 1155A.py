def solve(s, n):
    max_char = s[0]
    max_char_index = 0
    for i in range(n):
        if s[i] < max_char:
            return [max_char_index+1, i+1]
        else:
            max_char = s[i]
            max_char_index = i
    return [-1, -1]

n = int(input())
s = input()
start, end = solve(s, n)
if start == -1:
    print("NO")
else:
    print("YES")
    print(start, end)