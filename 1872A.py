from math import ceil
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a > b: a, b = b, a
    d = (b-a) / 2
    print(ceil(d/c))