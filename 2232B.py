for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    current_max = arr[0]
    ans = [current_max]
    carry = 0
    s = arr[0]
    for i in range(1, n):
        s += arr[i]
        arr[i] += carry
        if current_max > arr[i]:
            current_max = s // (i+1)
        carry = s - (current_max * (i+1))
        ans.append(current_max)
    print(*ans)