for _ in range(int(input())):
    k = int(input())
    arr = list(map(int, input().split()))
    opened = [-1, -1, -1]
    for _ in range(3):
        opened[k-1] = 0
        behind = arr[k-1]
        if behind == 0: 
            break
        else:
            k = behind
    print("YES" if sum(opened) == 0 else "NO")

