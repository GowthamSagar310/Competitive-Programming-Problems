n = int(input())
if n > 0:
    print(n)
else:
    n = -n
    last_digit = n % 10
    remove_last = n // 10
    remove_second_last = (n // 100) * 10 + last_digit
    print(max(-remove_last, -remove_second_last))
    