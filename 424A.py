n = int(input())
s = list(input())
small = s.count("x")
large = n-small
diff = (abs(small-large)) // 2
i = 0
if small < large:
    while i < n and diff:
        if s[i] == "X":
            s[i] = "x"
            diff -= 1
        i += 1
elif small > large:
    while i < n and diff:
        if s[i] == "x":
            s[i] = "X"
            diff -= 1
        i += 1
print((abs(small-large)) // 2)
print("".join(s))