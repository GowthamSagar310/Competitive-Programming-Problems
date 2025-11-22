n = int(input())
arr = list(map(int, input().split()))
m = int(input())
coupons = list(map(int, input().split()))

total = sum(arr)
sorted_arr = sorted(arr, reverse=True)

for c in coupons:
    # have to buy c items, eliminate the biggest possible one. 
    print(total-sorted_arr[c-1])
    