for _ in range(int(input())):
    s = input()
    """
    aaaaaaaa
    abbbbbbb
    abcdef
    """
    n = len(s)
    for i in range(1, n):
        if s[i] == s[i-1]:
            addition  = "a" if "z" < chr(ord(s[i])+1) else chr(ord(s[i])+1)
            s = s[:i] + addition + s[i:]
            break
    if len(s) == n: s += "a" if "z" < chr(ord(s[-1])+1) else chr(ord(s[-1])+1)
    print(s)