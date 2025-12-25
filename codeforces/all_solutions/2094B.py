# -3 -2 -1 0 1 2 3
#    -----------
#         --

for _ in range(int(input())):
    n, m, l, r = map(int, input().split())
    left_segment = right_segment = 0
    right_segment = min(m, r)
    m -= right_segment
    if m > 0:
        left_segment = min(m, abs(l))
        left_segment *= -1
    print(left_segment, right_segment)