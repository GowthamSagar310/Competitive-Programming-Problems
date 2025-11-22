for _ in range(int(input())):
    n = int(input())
    s = input()
    res = ""
    i = 0
    while i < n:

        j = i+1
        while j < n and s[i] != s[j]:
            j += 1
        
        res += s[i]
        i = j+1
    print(res)
