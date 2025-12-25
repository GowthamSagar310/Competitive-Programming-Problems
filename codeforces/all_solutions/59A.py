s = input()
lower_count = sum(1 if l.islower() else 0 for l in s)
upper_count = len(s) - lower_count
if lower_count >= upper_count:
    print(s.lower())
else:
    print(s.upper())
