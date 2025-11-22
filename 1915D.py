import sys
import math

def input(): return sys.stdin.readline().rstrip()

def solve(s, n):

    # CV
    # CVC
    # there cannot be VC, CC*, VV*
    
    # there is always a cut before C, if there is sufficient length
    consonants = ["b", "c", "d"]

    last_cut = n
    res = []
    for i in range(n-1, -1, -1):
        if s[i] in consonants:
            length = last_cut-i
            if length >= 2:
                # make a cut
                res.append(s[i:last_cut])
                last_cut = i
    print(".".join(reversed(res)))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        solve(s, n)
    
