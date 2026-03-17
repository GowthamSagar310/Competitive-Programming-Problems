n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

"""
when is it not possible ? 
if there is onle one zero and the remaining sequence is increasingly sorted

and also remember that there are no duplicated.
"""

def solve(a, b, n, k):
    if k > 1:
        return True
    else:
        index = a.index(0)
        a[index] = b[0]
        return a != sorted(a) 

print("Yes" if solve(a, b, n, k) else "No")