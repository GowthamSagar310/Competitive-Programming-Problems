from math import ceil
for _ in range(int(input())):
    x, y, k = map(int, input().split())

    """
    1. k*y sticks needed for k coals
    2. k sticks needed to be combined with k coals = k torches
    3. k+(k*y) sticks needed in total

    use 1 stick to gain x, net = x-1

    1 + d * (x-1) = k + (k * y)

    1 + d = 10
    d = 9 trades to get to required total of sticks
    + k trades to get coal
    """

    # d = ceil((k-1+k*y) / (x-1))
    # floating point issues

    a = k-1+k*y
    b = x-1
    d = (a+b-1)//b
    print(d + k)
