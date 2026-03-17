n, k = map(int, input().split())
arr = list(map(int, input().split()))
def solve(arr, n, k):
    candies = 0
    for i in range(n):
        k -= min(8, candies)
        candies -= min(8, candies)
        if k <= 0:
            return i
        candies += arr[i]
    return n if min(8, candies) >= k else -1
print(solve(arr, n, k))