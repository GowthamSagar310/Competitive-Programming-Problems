num, _, entity = input().split()
num = int(num)

"""
is 2016 leap year ? yes
total days = 366


today is wednesday. 
tomorrow is last day of 2015 - thursday
first day of 2016 - friday

1 M
2 T
3 W
4 T 
5 F
6 S 
7 S

F S S [M T W T F S S] ......... 

3 + [51 * 7] + 6
2 + [52 * 7]

we have extra friday, saturday
"""

if entity == 'week':
    if num == 5 or num == 6:
        print(53)
    else:
        print(52)
else:
    if num <= 29: print(12)
    elif num == 30: print(11)
    else: print(7)

