from math import ceil
for _ in range(int(input())):
    n, k = map(int, input().split())

    # n -> (1 + 1 + .. k-1) + (n-(k-1))
    # how many ones are being added each time ? k-1

    # if n == 1:
    #     print(0)
    # else:

    #     # we are added k-1 1's in every ops 
    #     # so how many (k-1)s can be fit into n-1? because the last one is anyway 1
    #     # (n - 1) / (k - 1)
    #     # if this is divided completely, we need one more op, so ceil 
    #     print(ceil((n-1) / (k-1)))

    print(ceil((n-1) / (k-1)))



