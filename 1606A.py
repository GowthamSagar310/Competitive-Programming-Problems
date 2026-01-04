# make ab and ba count same using minimum operations
# there is no deletes. 
# only replace characters with a or b

for _ in range(int(input())):
    s = list(input())
    n = len(s)

    # counts of ab, ba can only differ by 1
    # if they are equal = 0 ops = same string
    
    # think of "a" as going down
    # think of "b" as going up
    # if there are "aa" or "bb", stay there

    # with this analogy, 
    # if I start at a and end at a, that means I came to same place again = same counts
    # same for b
    
    # but if I start at a and end at b, there is some difference. 
    # If I make ends equal, then I always return at the same place

    s[0] = s[-1] # s[-1] = s[0] also works
    print("".join(s))
    