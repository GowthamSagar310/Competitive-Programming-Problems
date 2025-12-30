n = int(input())
total = (n * (n+1)) // 2
print(total - sum(list(map(int, input().split()))))
