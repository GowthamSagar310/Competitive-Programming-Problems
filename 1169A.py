n, a, x, b, y = map(int, input().split())

"""
a -> x
b -> y

1 2 3 4 5 

1 2 3 4
3 2 1 4

2 3 4 5 6 7 8 9 10 1
9 8 7 6 5 4 3 2 1 10

"""

def solve(n, a, x, b, y):
    curr_a, curr_b = a, b
    while curr_a != x and curr_b != y:
        curr_a = curr_a+1 if curr_a+1 <= n else 1
        curr_b = curr_b-1 if curr_b-1 > 0 else n
        if curr_a == curr_b:
            return True
    return False

print("YES" if solve(n, a, x, b, y) else "NO")

