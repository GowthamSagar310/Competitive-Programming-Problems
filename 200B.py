n = int(input())
drinks = list(map(int, input().split()))
print(sum([d / n for d in drinks]))