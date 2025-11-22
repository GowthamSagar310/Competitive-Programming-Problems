from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    # the point here is to make alice win somehow
    # it does not mean that both players play optimally

    # to make alice win somehow,
    # if every number repeats even number of times, 
    # alice can always loose
    # because bob can copy whatever alice is doing everytime
    
    # if there is atleast one number with odd frequency
    # we can make alice win
    # by choose all the even frequency numbers and at last choose the odd one.
    # if there are more odd frequency numbers,
    # if maximum number if repeated odd times -> choose the max
    # if maximum is repeated odd times -> choose other numbers first and 
    # let bob choose the first maximum, and alice can choose next maximum

    counter = Counter(arr)
    alice_wins = False
    for v in counter.values():
        if v & 1:
            alice_wins = True
            break
    print("YES" if alice_wins else "NO")
    
    

