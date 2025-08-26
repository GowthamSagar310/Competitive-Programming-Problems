def solve(a, b, xk, yk, xq, yq):
    points = {
        (+a, +b),
        (+a, -b),
        (+b, +a),
        (+b, -a),
        (-a, +b),
        (-a, -b),
        (-b, +a),
        (-b, -a),
    }
    k_moves = {(xk + dx, yk + dy) for dx, dy in points}
    return sum((xq + dx, yq + dy) in k_moves for dx, dy in points)

    
for _ in range(int(input())):
    a, b = map(int, input().split())
    xk, yk = map(int, input().split())
    xq, yq = map(int, input().split())
    print(solve(a, b, xk, yk, xq, yq))