# !! read this for python hashing problem 
# https://codeforces.com/blog/entry/101817
# https://codeforces.com/blog/entry/98994
# normal counter without this hash function will throw TLE
from collections import Counter
from random import getrandbits
RANDOM = getrandbits(32)
class Wrapper(int):
    def __hash__(self):
        return super().__hash__() ^ RANDOM

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    c = Counter(map(Wrapper, arr))
    m = sorted(c.values())
    uniq = len(m)
    i = 0
    while k and i < len(m)-1:
        f = m[i]
        if f > k: break
        k -= f
        uniq -= 1
        i += 1
    print(uniq)