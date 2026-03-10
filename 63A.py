import sys
input = sys.stdin.readline
n = int(input())
m = {
    "rat": 0,
    "woman": 1,
    "child": 1,
    "man": 2,
    "captain": 3
}

entries = []
for _ in range(n):
    name, role = input().split()
    entries.append((name, m[role]))
entries.sort(key=lambda x: x[1])

for name, _ in entries:
    print(name)
