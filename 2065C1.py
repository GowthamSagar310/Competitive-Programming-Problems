def solve(n, m, arr1, arr2):
    # a1 <= a2 <= a3 .. 
    pass


for _ in range(int(input())):
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    print("YES" if solve(n, m, arr1, arr2) else "NO")
