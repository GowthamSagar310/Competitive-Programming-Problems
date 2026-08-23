def solve(arr):
    n = len(arr)
    ans = 1
    most_recent_l = 0
    current_l = 0
    i = 0
    while i < n:
        start = i
        while i < n-1 and arr[i] < arr[i+1]:
            i += 1
        current_l = i-start+1
        if most_recent_l:
            ans = max(ans, min(most_recent_l, current_l), current_l//2)
        else:
            ans = max(ans, current_l // 2)
        most_recent_l = current_l
        i += 1
    return ans 

arr = [1, 1, 1, 1, 1, 2, 3, 4, 1, 1, 1, 2, 3, 4, 5, 6]
print(solve(arr))