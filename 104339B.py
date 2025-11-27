weights = list(map(int, input().split()))

def solve(weights):
    total = sum(weights)
    for i in range(1, 15):
        j = 0
        left = 0
        while i:
            if i & 1:
                left += weights[j]
            j += 1
            i >>= 1
        if left == total - left:
            return True
    return False
print("YES" if solve(weights) else "NO")
