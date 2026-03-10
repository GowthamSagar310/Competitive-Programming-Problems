s = input()
def solve(s):
    for i in range(1, len(s)-1):
        if (
            all(val != '.' for val in [s[i-1], s[i], s[i+1]]) and 
            (s[i-1] != s[i] and s[i] != s[i+1] and s[i+1] != s[i-1])
        ):
            return True
    return False
print("Yes" if solve(s) else "No")