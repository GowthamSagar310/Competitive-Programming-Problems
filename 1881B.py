"""
1 3 2

(3-1) // 1
(2-1) // 1

6 36 12
(36-6) // 6 = 5

36 = 6 + 30 
   = 6 + 6 + 24
"""

for _ in range(int(input())):
    a, b, c = sorted(list(map(int, input().split())))
    ops = 4
    if b % a == 0 and c % a == 0:
        ops = ((b-a) // a) + ((c-a) // a)
    print("YES" if ops <= 3 else "NO")

