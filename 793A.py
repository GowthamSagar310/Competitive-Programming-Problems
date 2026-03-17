n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def solve(arr, n):
    if n == 1: return 0
    count = 0
    for i in range(n):
        if (arr[i]-arr[0]) % k != 0: return -1
        count += (arr[i]-arr[0]) // k
    return count

print(solve(arr, n))