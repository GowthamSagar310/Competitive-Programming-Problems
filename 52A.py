n = int(input())
arr = list(map(int, input().split()))
ones, twos = arr.count(1), arr.count(2)
threes = n - ones - twos
print(sum(sorted([ones, twos, threes])[:2]))