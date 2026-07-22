n, m = map(int, input().split())
map = {}
for _ in range(m):
    a, b = input().split()
    if len(a) > len(b):
        map[a] = b
sentence = input().split()
ans = []
for word in sentence:
    ans.append(map.get(word, word))
print(" ".join(ans))