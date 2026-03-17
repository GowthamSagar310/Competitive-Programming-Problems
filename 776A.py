initial = input().split()
n = int(input())

for _ in range(n):
    print(*initial)
    killed, replaced = input().split()
    for i, name in enumerate(initial):
        if name == killed:
            initial[i] = replaced
            break

print(*initial)