for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # atleast one odd field must be there. 
    # max odds can be taken, leaving small odds

    even = []
    odd = []
    for n in arr:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    even.sort()
    odd.sort()
    if odd:
        total = sum(even)
        count = ((len(odd)-1) // 2) + 1
        print(total + sum(odd[-count:]))
    else:
        print(0)