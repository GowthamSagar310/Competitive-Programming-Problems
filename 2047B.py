for _ in range(int(input())):
    n = int(input())
    s = list(input())
    freq = {}
    maxi = 0
    for l in s:
        freq[l] = freq.get(l, 0) + 1
        if freq[l] > maxi:
            maxi = freq[l]
            maxi_l = l
    

    for i, l in enumerate(s):
        if l != maxi_l:
            s[i] = maxi_l
            break 

    print("".join(s))
