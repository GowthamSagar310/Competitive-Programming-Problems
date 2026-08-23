from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))

    """
    - choose two numbers such that they are x, y
    """
    
    def get_seq(x, y):
        seq = [x, y]
        for _ in range(n-2):
            if y == 0: return seq
            next = x % y
            x = y
            y = next
            seq.append(next)
        return seq

    b.sort(reverse=True)
    found = False
    ans = [-1]
    for i in range(n):
        for j in range(i+1, n):
            x, y = b[i], b[j]
            seq = get_seq(x, y)
            if b == seq:
                found = True
                ans = [x, y]
        if found: break
    print(*ans)
    

