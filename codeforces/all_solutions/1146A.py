s = input()
n = len(s)
a_count = s.count("a")
if a_count > n // 2:
    print(n)
else:
    remaining_char_count = n-a_count
    difference = remaining_char_count-a_count
    print(n-difference-1)
