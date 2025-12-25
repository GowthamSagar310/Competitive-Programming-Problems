from sys import stdin
input = stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    curr_sum = 0
    curr_max = 0
    total = 0
    for num in arr:
        curr_sum += num
        curr_max = max(curr_max, num)
        if curr_max * 2 == curr_sum:
            total += 1
    print(total)

# we can use a set to check if the curr_sum // 2 is present in seen.
# seen.add(num), curr_sum // 2 in seen, then total += 1
# why ? 
# we are trying to find a number x, which is sum of all other numbers till now 
# x + x = curr_sum
# x = curr_sum // 2
# but gives TLE !! because there is much simpler solution

# but we have to observe that if 
# x + (x -> remaining elements sum) = curr_sum 
# then x must be the maximum value till now. 

# python sets are dicts underneath (hashmaps)
# average case O(1) for insertion, deletion, lookup
# worst case O(N) when hash collisions
# 
# in c++, 
# ordered set -> implemented as trees -> avg: logn | worst: logn
# unordered set -> implemented as hashmap -> avg: O(1) | worst: logn