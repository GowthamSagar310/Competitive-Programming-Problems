from collections import Counter
for _ in range(int(input())):
    s = input()


    """
    - string only contains digits from 1-4
    - subsequence of the digits should not form a multiple of 4
    
    observations
    - 4 should not be present.
    - 1 before 2 should not be present.
    - 3 before 2 should not be present.

    4 
    12
    24
    32
    44

    """

    # this wont work
    # because we are trying to remove all 1s, 3s
    # but we dont have to. 13222211
    # only the 1, 3 at the first must be removed
    # if the 1, 3 are after all twos, then dont remove them
    # n = len(s)
    # c = Counter(s)
    # remove = c['4']
    # for i in range(n):
    #     if s[i] == '1' or s[i] == '3':
    #         if c['2']:
    #             if c['1'] + c['3'] >= c['2']:
    #                 remove += c['2']
    #                 c['2'] = 0
    #             else:
    #                 remove += c['1'] + c['3']
    #     elif s[i] == '2' and c['2']:
    #         c['2'] -= 1
    # print(remove)


    # 22221111333
    # this is the best sequence where nothing have to be removed
    # we need to find the longest length of the sequence like this
    # we need to remove the remaining things


    # the longest subsequence is found by using prefix, suffix
    # prefix is shifted to right 
    # suffix is shifted to left
    # for easier code 
    
    n = len(s)
    fours = s.count('4')
    prefix = [0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + (s[i] == '2')

    suffix = [0] * (n+1)
    for i in range(n-1, -1, -1):
        suffix[i] = suffix[i+1] + (s[i] in '13')
    
    longest = 0
    for i in range(n+1):
        longest = max(longest, prefix[i] + suffix[i])

    non4 = n-fours
    print(fours + (non4 - longest))

    
