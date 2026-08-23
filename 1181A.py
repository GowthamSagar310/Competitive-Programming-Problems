x, y, z = map(int, input().split())
print((x // z) + (y // z) + (((x % z) + (y % z)) // z), end = " ")
print(max(min(x % z, y % z) - ((x % z) + (y % z)) % z, 0))
