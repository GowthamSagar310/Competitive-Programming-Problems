s = input()
index = s.index("^")
left, right = 0, 0
for i, l in enumerate(s):
    if l.isnumeric():
        if i < index:
            left += int(l) * (index-i)
        else:
            right += int(l) * (i-index)

if left < right: 
    print("right")
elif left > right:
    print("left")
else:
    print("balance")