n, m ,k = map(int, input().split())

"""
n days
m bowls, k plates

type 1 -> bowls
type 2 -> bowls / plates


total += max(ones-m, 0)
total += max(twos-(k + max(m-ones, 0)), 0)


if ones >= m:
    total += ones - m 
    total += twos
else:
    total += ones
    total += max(twos-(m-ones+k), 0)


"""

arr = list(map(int, input().split()))
ones = arr.count(1)
twos = n - ones
total = 0
total += max(ones-m, 0)
total += max(twos-(k + max(m-ones, 0)), 0)
print(total)