def is_there_valid(l, r):
    while r-l > 1:
        if s[r] == "1":
            return r
        r -= 1
    return -1

for _ in range(int(input())):
    
    n = int(input())
    s = input()

    # if for every 1, there is a pair on the other side
    # mean left and right which are not adjacent.

    ones = s.count("1")
    if ones & 1:
        print("NO")
    elif ones == 2:
        index = s.index("1")
        if s[index+1] == "1":
            print("NO")
        else:
            print("YES")
    else:
        print("YES")