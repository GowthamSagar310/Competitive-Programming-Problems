x = int(input())
count = x // 5 + (1 if x % 5 != 0 else 0)
print(count)