months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

month, day = map(int, input().split())
num_days = months[month]
total_days = num_days + (day-1) # includes dummy days because the first day might start at any day of the week.
# rows_needed = total_days // 7 + (0 if total_days % 7 == 0 else 1)

# neat trick
# ceil(x // n) = floor(x-1 // n) + 1
# we did x-1 because, it fixes the cases where x % n == 0
rows_needed = (total_days-1) // 7 + 1

print(rows_needed)