s = input()
def solve(s):
    for l in s:
        if l in ["H", "Q", "9"]:
            return True
    return False
print("YES" if solve(s) else "NO")