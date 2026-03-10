n = int(input())
arr = list(map(int, input().split()))
arr.sort()
s = set(arr)


def solve(n, arr):
    for i in range(n):
        if arr[i] + 1 in s and arr[i] + 2 in s:
            return True
    return False

print("YES" if solve(n, arr) else "NO")