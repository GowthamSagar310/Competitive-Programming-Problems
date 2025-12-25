n, k = map(int, input().split())    
arr = list(map(int, input().split()))

count = sum(1 if val + k <= 5 else 0 for val in arr)
print(count // 3)