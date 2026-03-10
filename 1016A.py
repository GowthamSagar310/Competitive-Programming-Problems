n, m = map(int, input().split())
arr = list(map(int, input().split()))
carry = 0
for i in range(n):
    names = arr[i]
    if carry + names >= m:
        names -= (m-carry)
        turns = 1 + (names // m)
        carry = names % m
        print(turns, end = " ")
    else:
        carry += names
        print(0, end = " ")


        

