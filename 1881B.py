# UNSOLVED 
def get_max(m):
    keys = sorted(m.keys(), reverse=True)
    return keys[0], -1 if len(keys) == 1 else keys[1]

def solve(a, b, c):
    m = {a: 1, b: 1, c: 1}
    ops = 3
    while ops:
    
        maxi1, maxi2 = get_max(m)
        if maxi2 == -1:
            return "YES"
        
        # convert maxi1 interms of maxi2
        diff = maxi1 - maxi2
        
        m[maxi1] -= 1
        if m[maxi1] == 0: del m[maxi1]
        m[maxi2] += 1
        m[diff] = m.get(diff, 0) + 1
    
        ops -= 1
    
    return "YES" if len(m) == 1 else "NO"

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(solve(a, b, c))

