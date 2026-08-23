def get_luck(x):
    sx = str(x)
    return ord(max(sx))-ord(min(sx))

for _ in range(int(input())):
    l, r = map(int, input().split())
    
    """
    - the idea here is that, if l and r are farther by 100 or more 
    - there are always a cycle in last two digits of the numbres 
    - from 00 -> 99
    - so it is enough to check for 100 numbers from l, as long as it is <= r
    """

    best_num, max_luck = l, get_luck(l)
    for i in range(l+1, min(r, l+100)+1):
        luck = get_luck(i)
        if luck > max_luck:
            max_luck = luck
            best_num = i
    print(best_num)


