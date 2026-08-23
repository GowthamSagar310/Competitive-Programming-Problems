for _ in range(int(input())):
    s = input()
    """
    - alice wants to make it large and remove 0s
    - bob wants to make it small and remove 1s
    """
    z_index = s.find("0")
    o_index = s.find("1")
    ans = ""
    for i in range(len(s)):
        if i != z_index and i != o_index:
            ans += s[i]
    print(ans)