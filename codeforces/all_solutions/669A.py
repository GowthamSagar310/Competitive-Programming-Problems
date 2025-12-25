n = int(input())

# how many combinations or 1-2 can be made ? 

print(2 * (n // 3) + (0 if n % 3 == 0 else 1))