for _ in range(int(input())):
    s = list(input())
    n = len(s)
    for i in range(n):
        if i & 1:
            j = 25
            while chr(j + ord('a')) == s[i]:
                j -= 1
            s[i] = chr(j + ord('a'))
        else:
            j = 0
            while chr(j + ord('a')) == s[i]:
                j += 1
            s[i] = chr(j + ord('a'))        
    print("".join(s))
