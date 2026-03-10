n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
mini = min(val if val % 2 else float("inf") for val in arr)
if total % 2 == 0:
    print(total)
else:
    print(total - mini)