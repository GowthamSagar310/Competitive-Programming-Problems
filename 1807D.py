for _ in range(int(input())):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    prefix_arr = [arr[0]]
    for i in range(1, n):
        prefix_arr.append(prefix_arr[-1] + arr[i])
    total = prefix_arr[-1]

    # what is the sum between l, r inclusive
    # [........l.......r......]
    # .................. sum till r 
    # ......... sum till l-1

    for _ in range(q):
        l, r, k = map(int, input().split())
        l -= 1
        r -= 1

        # range_sum            
        range_sum = prefix_arr[r]
        range_sum -= prefix_arr[l-1] if l-1 >= 0 else 0

        # replace [l..r] with k
        new_sum = (total - range_sum) + (k * (r-l+1))

        print("YES" if new_sum & 1 else "NO")
        
