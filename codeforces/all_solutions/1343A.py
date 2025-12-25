import sys
import math

def input(): return sys.stdin.readline().rstrip()

def solve(n):

    # x + 2x + 4x + ... 
    # a = x, r = 2, number of terms = k
    # s = a (r^k-1) / (r-1)
    # s = x (r^k - 1)
    # n = x ((2^k) - 1)
    
    # because x is an integer, n should be divisible by (2^k)-1 -> 3, 7, 15..
    # n <= 10^9
    # 2^10 ~ 10^3 
    # n <= 10^9 < (2^10)^3
    # n < 2^30
    # k can only less than 30

    for k in range(2, 30):
        if n % ((2 ** k)-1) == 0:
            print(n // ((2 ** k)-1))
            break    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        solve(n)
