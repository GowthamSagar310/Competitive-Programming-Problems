n = int(input())

skills = []
learned = set()
for i in range(1, n+1):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    skills.append((a, b, i))
    if a == 0 and b == 0:
        learned.add(i)
skills.sort(key=lambda x: (x[0], x[1]))
for j in range(1, n+1):
    a, b, num = skills[j-1]
    if a in learned or b in learned:
        learned.add(num)

print(len(learned))