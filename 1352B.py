for _ in range(int(input())):
    n, k = map(int, input().split())

    # check if it is possible to construct odd numbers
    # minimum possible odd = 1
    # if choose k-1 1s and the last term is also odd, then it is possible
    # if the last term is even, if it not possible to distribute
    # such that everything is an odd, there will be atleast one even
    n1 = n-k+1
    if (n1 > 0 and n1 & 1):
        print("YES")
        print(*([n1] + [1]*(k-1)))
        continue
    
    # check if it is possible to construct even numbers
    # minimum possible odd = 2
    # if choose k-1 2s and the last term is also even, then it is possible
    n2 = n-2*k+2
    if (n2 > 0 and n2 % 2 == 0):
        print("YES")
        print(*([n2] + [2]*(k-1)))
        continue

    print("NO")