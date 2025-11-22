k, n, w = map(int, input().split())

# k + 2k + 3k + 4k .. wk
# k ( 1 + 2 + 3 + 4 .. w)
# max(0, n- (k ((w) * (w+1)) // 2))

print(max(0, (k * ((w * (w+1)) // 2))-n))