def solve(n, m, arr1, arr2):
    pass

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    # a1 <= a2 <= a3 .. 
    print("YES" if solve(n, m, arr1, arr2) else "NO")
