# remove digits
# make it divisible by 25
# minimum number of removals ? 

"""
25,75,125,175,... == (2/7) before 5
50,100,150,200,250... == (0,5) before 0

so the idea here is, 
we have to find 25, 75, 00, 50 in the given number
and try to make these the last values in the number
"""

# def solve(n):
    # digits = str(n)
    # l = len(digits)
    # ops = float("inf")
#     last_two = last_seven = last_five = last_zero = -1
#     for i in range(l):
#         if digits[i] == "0": 
#             if last_zero != -1: ops = min(ops, l-last_zero-2)
#             if last_five != -1: ops = min(ops, l-last_five-2)
#             last_zero = i

#         if digits[i] == "5":
#             if last_two != -1: ops = min(ops, l-last_two-2)
#             if last_seven != -1: ops = min(ops, l-last_seven-2)
#             last_five = i

#         if digits[i] == "2": last_two = i
#         if digits[i] == "7": last_seven = i
#     return ops

# we want to make the farthest "00", "50", "25", "75"
# meaning we want to look for these values at the end
# it makes sense to travel from backwards
# because it does not matter how many 25 we want before the last 25
# we are always going to choose the last one because it gives minimum ops
def solve(num):
    n = str(num)
    l = len(n)
    ops = float("inf")
    targets = ["00", "25", "50", "75"]
    for t in targets:
        d1, d2 = t[0], t[1]

        # from last where is the first d2
        idx2 = -1
        for i in range(l-1, -1, -1):
            if n[i] == d2:
                idx2 = i
                break
        
        if idx2 == -1: continue

        # from idx2 to start, where is the first d1 
        idx1 = -1
        for i in range(idx2-1, -1, -1):
            if n[i] == d1:
                idx1 = i
                break

        if idx1 == -1: continue
        ops = min(ops, l-idx1-2)
    return ops 

for _ in range(int(input())):
    n = int(input())
    print(solve(n))
        
