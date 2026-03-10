"""

there are n days in a year
5 + 2 

LLBBBBBL

start the year with offs. 


start the year with work-days

BBBBBLLBBBBBL

"""
n = int(input())
if n <= 7:
    mini = max(0, n-5)
    maxi = min(2, n)
else:
    mini = 2 * (n // 7) + max((n % 7)-5, 0)
    maxi = 2 + 2 * ((n-2) // 7) + max(((n-2) % 7)-5, 0)
print(*[mini, maxi])