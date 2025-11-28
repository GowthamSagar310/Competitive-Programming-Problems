for _ in range(int(input())):
    n = int(input())
    s = input()

    # the idea here is that we need to check
    # for substrings with same symbol, with > or < 
    # say there is a substring with "<" 5 times, then numbers should in form of 1 2 3 4 5 6 (5 + 1 numbers)
    # there is no other way around this
    # so if the biggest is this
    # then the middle elements, meaning movement from > to < or < to > 
    # can be filled in with the same numbers
    # or more importantly if 
    # s[i-1] == ">" and s[i] == "<" we know next will be increasing choosing minimum possible number 
    # s[i-1] == ">" and s[i] == ">" we know we still need to decrease, so decrease by one, continue the flow
    # 
    # s[i-1] == "<" and s[i] == ">" we know that next will be decreasing so choose the maximum possible number (which is m + 1 where m is the length of longest substring)
    # s[i-1] == "<" and s[i] == "<" we know we still need to increase, so increase by one, continue the flow
    
    max_streak = curr_streak = 1
    for i in range(1, n):
        if s[i] == s[i-1]:
            curr_streak += 1
        else:
            max_streak = max(max_streak, curr_streak)
            curr_streak = 1
    max_streak = max(max_streak, curr_streak)
    print(max_streak + 1)