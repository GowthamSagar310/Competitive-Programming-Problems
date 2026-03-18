from collections import defaultdict
n, q = map(int, input().split())
answers = []
for _ in range(n):
    answers.append(input())
scores = list(map(int, input().split()))

total = 0
for j in range(q):
    maxi = 1
    count = 1
    options = defaultdict(int)
    for i in range(n):
        options[answers[i][j]] += 1
    total += max(options.values()) * scores[j]

print(total)