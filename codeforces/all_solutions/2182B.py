def solve(a, b, a_turn):
    need = 1
    layers = 0
    while a >= 0 and b >= 0:
        if a_turn:
            if a >= need:
                a -= need 
                layers += 1
            else:
                break
            a_turn = False
        else:
            if b >= need:
                b -= need
                layers += 1
            else:
                break
            a_turn = True
        need *= 2
    return layers

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(max(solve(a, b, True), solve(a, b, False)))