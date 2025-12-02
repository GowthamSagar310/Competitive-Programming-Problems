n = int(input())
arr = list(map(int, input().split()))

# alice's party = arr[0]

def solve(n, arr):
    curr = arr[0]
    total = sum(arr)
    res = [1]
    if curr > (total // 2):
        return [1]
    else:
        for i in range(1, n):
            if arr[0] >= 2 * arr[i]:
                curr += arr[i]
                res.append(i+1)
            if curr > (total // 2):
                return res
        return []

res = solve(n, arr)
if res:
    print(len(res))
    print(*res)
else:
    print(0)