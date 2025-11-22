for _ in range(int(input())):
    n = int(input())
    digits = []
    while n:
        digits.append(n % 10)
        n //= 10
    print(min(digits))
