"""

j - aj != i - a1
ai - aj != i - j

ai - aj != < 0 
ai - aj >= 0

"""


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print(*arr)