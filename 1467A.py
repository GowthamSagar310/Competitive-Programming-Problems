
"""
1. should pause one of the panels at each second. 
2. each second the digit on the panel changes to the next number. 
3. we want the largest number possible. 

n = 5
9 8 7 6 5

n = 11
9 8 7 6 5 4 3 2 1 0 9

"""

for _ in range(int(input())):
    n = int(input())
    s1 = "989"
    s2 = "0123456789"

    if n <= 3:
        print(s1[:n])
    else:
        print(s1 + s2[:] * ((n-3)//10) + s2[:(n-3)%10])

    # instead of hardcoding s2    
    # for i in range(n-3):
    #   print(i % 10)