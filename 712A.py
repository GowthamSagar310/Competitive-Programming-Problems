n = int(input())
arr = list(map(int, input().split()))
b = []
for i in range(n-1):
    b.append(str(arr[i]+arr[i+1]))
b.append(str(arr[-1]))
print(" ".join(b))