n, a, b = map(int, input().split())

"""

aaaaa        bbbbbbb
....................

aaaaabbbbbbbbbbbbbbb
....................

aaaaaaaaaaaaaaaaaaaa
....................

bbbbbbbbbbbbbbbbbbbb
....................

    bbbbbbbbbbbbbbbb
aaaaaaa
....................
"""

if b+a < n: 
    total_pos = b+1
else:
    overlap = b+a-n
    b -= overlap
    total_pos = b
print(total_pos)



