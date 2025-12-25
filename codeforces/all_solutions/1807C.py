def solve(s):
    for i in range(n):
        j = i+1
        while j < n and s[i] != s[j]:
            j += 1
        if j < n and s[i] == s[j] and (j-i-1) % 2 == 0:
            return "NO"
    return "YES"

for _ in range(int(input())):
    n = int(input())
    s = input()

    # if two consecutive chars - NO
    # if two repeating chars are > even distance apart - NO
    # 
    # all different chars - YES
    
    print(solve(s))