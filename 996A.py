n = int(input())
notes = 0
for val in [100, 20, 10, 5, 1]:
    while n >= val:
        notes += (n // val)
        n -= val * ((n // val))
print(notes)