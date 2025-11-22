r, c = map(int, input().split())
print(r-1 if c == 1 else r * (c-1))