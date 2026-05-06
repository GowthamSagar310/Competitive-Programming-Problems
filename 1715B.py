"""
array length = n 
non-negative integers can include zero
divide each element with k 
beauty = sum of all floor(arr[i]/k)
sum of elements = s

a1 + a2 + a3 .... an = s
a1//k + a2 // k + .... = b


if one value can be giving the required beauty, can we adjust the sum with remaining values ? 
using zeroes or < k values ?
"""

for _ in range(int(input())):
    n, k, b, s = map(int, input().split())
    first_val = b * k
    if first_val > s:
        # if the max value is greater than sum,
        # we cannot reduce this to get the required beauty. 
        print(-1)
    else:
        sum_needed = s-first_val
        ans = [first_val]

        while sum_needed and len(ans) < n:
            next_val = min(sum_needed, k-1)
            sum_needed -= next_val
            ans.append(next_val)

        if sum_needed and (sum_needed + ans[0]) // k == b:
            ans[0] += sum_needed
            print(*ans)
        elif sum_needed == 0:
            ans.extend([0] * (n-len(ans)))
            print(*ans)
        else:
            print(-1)
