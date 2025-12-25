"""
--__-_---

---___---
3 * 3 * 3

-----___-
5 * 3 * 1
"""

# for _ in range(int(input())):
#     n = int(input())
#     s = input()
#     d = s.count("-")
#     u = n-d
#     if u < 1 or d < 2:
#         print(0)
#     else:
#         left_dashes = d // 2
#         right_dashes = d // 2 + (d & 1)
#         print(left_dashes * u * right_dashes)


# simplified
for _ in range(int(input())):
    n = int(input())
    s = input()
    d = s.count("-")
    u = n-d
    left_dashes = d // 2
    right_dashes = d - left_dashes
    print(left_dashes * u * right_dashes)