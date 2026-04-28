s = input()

def all_up(s): return all(l.isupper() for l in s)
def except_first(s):
    return all(l.isupper() for l in s[1:])

if all_up(s) or except_first(s):
    res = []
    for l in s:
        if l.islower(): res.append(l.upper())
        else: res.append(l.lower())
    print("".join(res))
else:
    print(s)
