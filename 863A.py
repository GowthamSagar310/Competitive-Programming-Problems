x = input()
n = len(x)
if x[-1] == "0":
    i = n-1
    while x[i] == "0": 
        i -= 1
    zeros = n-1-i
    x = "0" * zeros + x
print("YES" if x == x[::-1] else "NO")
    

