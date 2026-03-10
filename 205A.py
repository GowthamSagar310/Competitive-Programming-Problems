n = int(input())
arr = list(map(int, input().split()))
mini = min(arr)
if arr.count(mini) > 1:
    print("Still Rozdil")
else:
    print(arr.index(mini)+1)