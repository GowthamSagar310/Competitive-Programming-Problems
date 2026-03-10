n, s = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s -= 1
if a[0] != 0:

    if a[s] == 1:
        print("YES")
    elif b[s] == 1:

        # is there a stopping station to change tracks
        i = s+1
        found = False
        while i < n:
            if a[i] == 1 and b[i] == 1:
                found = True
                break
            i += 1
        
        print("YES" if found else "NO")

    else:
        print("NO")
else:
    print("NO")
