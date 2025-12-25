from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = input()

    # substring should not contain map or pie
    # common letter is p
    # if there is no p, there is map or pie 
    # see if removing p is better or 
    # removing (m, i) (m, e) (a, i) (a, e) is better

    freq = Counter(s)
    
    # this works only with subsequences can be considered
    # print(min(
    #     [
    #         freq["p"],
    #         freq["m"] + freq["i"],
    #         freq["m"] + freq["e"],
    #         freq["a"] + freq["i"],
    #         freq["a"] + freq["e"]
    #     ]
    # ))

    # in the above code for s = "amp", ans = 1
    # but we dont have to remove anything. 
