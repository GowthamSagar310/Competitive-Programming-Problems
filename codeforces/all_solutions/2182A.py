"""
atleast one of the conditions is met -> then new year string

1. "2026" in s 
2. "2025" not in s


what are the minimum number of operations to make the string s -> new year


1. if 2026 present in s, 0 ops 
2. if 2025 not present in s, 0 ops
3. after this, it means that (there is no 2026) or (there is 2025)
4. if 2025 is present -> it takes one op to convert to 2026 -> 1
5. if there is no 2026 and we made it this far, then it is not possible. 
"""

for _ in range(int(input())):
    n = int(input())
    s = input()
    present_2026 = "2026" in s
    present_2025 = "2025" in s
    if present_2026 or (not present_2025):
        print(0)
    else:
        print(1)