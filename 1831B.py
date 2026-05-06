# from collections import defaultdict

# def get_blocks(arr):
#     blocks = defaultdict(list)
#     l = r = 0
#     while r < n:
#         if arr[r] != arr[l]:
#             blocks[arr[l]].append([l, r-1])
#             l = r
#         r += 1
#     blocks[arr[l]].append([l, r-1])
#     return blocks

# def get_maximum(a_blocks, b_blocks):
#     maximum = 1
#     for k, blocks in a_blocks.items():
#         for l1, r1 in blocks:
#             for l2, r2 in b_blocks[k]:
#                 if not (l2-r1 > 1):
#                     maximum = max(maximum, r1-l1+1 + r2-l2+1)
#             maximum = max(maximum, r1-l1+1)
#     return maximum

# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     maximum = 1

#     a_blocks = get_blocks(a)
#     b_blocks = get_blocks(b)

#     maximum = max(maximum, get_maximum(a_blocks, b_blocks))
#     maximum = max(maximum, get_maximum(b_blocks, a_blocks))

#     print(maximum)


# instead of calculating for each block, we can just take the maxmimum blocks. 
# that is enough because we can always arrange them next to each other. 
# longest subarray with value x only + longest subrray with value x only in b
# this can always be achieved. 
# so instead of storing the blocks and checking for overlap
# we can just check for maximums. 


from collections import defaultdict


def get_blocks(arr):
    blocks = defaultdict(int)
    l = r = 0
    while r < n:
        if arr[r] != arr[l]:
            blocks[arr[l]] = max(blocks[arr[l]], r-l)
            l = r
        r += 1
    blocks[arr[l]] = max(blocks[arr[l]], r-l)
    return blocks


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    maximum = 1

    a_blocks = get_blocks(a)
    b_blocks = get_blocks(b)

    for a_val, max_a in a_blocks.items():
        maximum = max(maximum, max_a + b_blocks[a_val])
    
    for b_val, max_b in b_blocks.items():
        maximum = max(maximum, max_b + a_blocks[b_val])

    print(maximum)
