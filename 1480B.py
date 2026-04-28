from math import ceil

def solve(A, B, n, a, b):
    damage = 0
    for ai, bi in zip(a, b):
        rounds = ceil(bi / A)
        damage += rounds * ai
    
    max_monster_attack = max(a)

    # when the last monster is being attacked, we still need to have some health. cannot be zero
    # but if the B is too low, before this itself, because the health of some monster too large, 
    # B will negative and even before max_monster_attack, it dies

    return B - damage + max_monster_attack > 0
        
    
for _ in range(int(input())):
    A, B, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("YES" if solve(A, B, n, a, b) else "NO")
    """
    B is initial health of hero
    A is attack of hero

    bi is initial health of monster
    ai is attack of monster

    B-ai
    bi-A

    for the last monster, it does not matter if the hero died. the monster should die too. 
    so if i handle the monster with largest attack at last, I will always win. 
    """



