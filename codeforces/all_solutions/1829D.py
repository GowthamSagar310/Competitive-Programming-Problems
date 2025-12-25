def solve(n, m):
    if n % 3 == 0:
        prev = [n]
        while prev:
            curr = []
            for val in prev:
                if val % 3 == 0:
                    x = val // 3
                    if x == m or 2 * x == m:
                        return "YES"
                    curr.append(x)
                    curr.append(2 * x)
            prev = curr
    return "YES" if n == m else "NO"

def recur(n, m):
    if n == m: return True
    if n % 3 != 0: return False
    return recur(n // 3, m) or recur((2*n)//3, m)

for _ in range(int(input())):
    n, m = map(int, input().split())


    # n = x + 2*x 
    # n = 3*x
    # n must be divisible by 3 to split
    # after spliting, x and 2x

    print("YES" if recur(n, m) else "NO")