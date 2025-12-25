def solve(s1, s2, s3):
    p = 0 
    for word in s1:
        if word in s2 and word in s3:
            p += 0
        elif word in s2 or word in s3:
            p += 1
        else:
            p += 3
    return p 

for _ in range(int(input())):
    n = int(input())
    
    w1 = set()
    w2 = set()
    w3 = set()
    
    for word in input().split(): w1.add(word)
    for word in input().split(): w2.add(word)
    for word in input().split(): w3.add(word)

    p1 = solve(w1, w2, w3)
    p2 = solve(w2, w1, w3)
    p3 = solve(w3, w1, w2)

    print(p1, p2, p3)