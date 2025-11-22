n = int(input())
arr = list(map(int, input().split()))
maxi = max(arr)
print(sum([maxi-num for num in arr]))