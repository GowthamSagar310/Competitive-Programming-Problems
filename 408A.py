n = int(input())
queues = list(map(int, input().split()))

print(min(sum(list(map(int, input().split()))) * 5 + q * 15 for q in queues))
