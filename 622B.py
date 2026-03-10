h, m = map(int, input().split(":"))

add_m = int(input())
h_add1, add_m = divmod(add_m, 60)

h_add2, new_m = divmod(m+add_m, 60)

_, new_h = divmod(h + h_add1 + h_add2, 24)

print("{:02d}:{:02d}".format(new_h, new_m))
