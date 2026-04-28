# n = int(input())

# """
# - if the number itself is fibanocci 0, 0, n
# - if not, what is the nearest fibanocci number
# """
# def nearest_fibanocci(n):
#     if not n: return 0
#     a, b = 0, 1
#     while b + a <= n:
#         temp = a+b
#         a = b
#         b = temp
#     return b

# nf1  = nearest_fibanocci(n)
# nf2 = nearest_fibanocci(n-nf1)
# nf3 = nearest_fibanocci(n-nf1-nf2)
# print(nf1, nf2, nf3)

# we dont have to solve this problem
# the input itself says that the number is fibanocci
# so we can always print 0, 0, n