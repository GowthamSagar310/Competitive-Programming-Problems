n = int(input())
arr = list(map(int, input().split()))

# if neg_count == odd, we need one more -1
# which is easier to get from 0. 
# if there are no zeroes, but the neg_count is odd
# we need to make extra effort of +2 to convert any 1/ -1 appropriately

# if neg_count == even, make all of them -1
# zeroes will anyway be converted to 1

ops = 0

neg_count = len(list(filter(lambda x: x < 0, arr)))
zero_present = 0 in arr
for i in range(n):
    ops += abs(abs(arr[i])-1)

if neg_count % 2 != 0 and not zero_present:
    ops += 2

print(ops)