for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    total = 0
    index = n // 2 + n % 2

    # just pair bigger elements with smaller ones
        
    initial = n*k # start at end index + 1 
    diff = (n-index)+1 # move forward diff distance
    initial -= diff # initial
    for j in range(initial, -1, -diff):
        total += arr[j]
        k -= 1
        if not k: 
            # we need do this only k times because
            # we need to have k arrays
            break
    print(total)
