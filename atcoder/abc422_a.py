i, j = map(int, input().split("-"))
if j < 8:
    j += 1
else:
    if i < 8:
        j = 1
        i += 1
print(str(i) + "-" + str(j))