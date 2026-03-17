n = int(input())
s = map(int, list(input()))
carry = 1
change = 0
for bit in s:
    if carry != 0:
        change += 1
    carry = 1 if bit + carry == 2 else 0
print(change)