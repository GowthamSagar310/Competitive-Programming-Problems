for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = [0] * (100)
    for v in arr: freq[v] += 1
    possible = True
    for num in range(1, 100):
        if freq[num] > freq[num-1]:
            possible = False
            break
    print("YES" if possible else "NO")

