n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print ("No" if sum(arr1) < sum(arr2) else "Yes")