s = input()

# there cannot be numbers other than 1, 4
# there cannot be three consecutive 4s
# first digit cannot be 4 

def solve(s):
    if s[0] == "4":
        return "NO"
    count = 0
    for l in s:
        if l != "1" and l != "4":
            return "NO"
        if l == "4":
            count += 1
            if count > 2:
                return "NO"
        else:
            count = 0
    return "YES"

print(solve(s))