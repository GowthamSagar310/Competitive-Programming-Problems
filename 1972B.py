def solve(s):
    """
    - players always choose the "U"
    - in each move, we remove one "U"
    - UUD, UUU, DUD, DUU
    -  DU,  DD,  UU,  UD
    -  -1   -3   +1   -1
    - the change is always odd. 
    - meaning the initial amount of k is always changing by odd.
    - so the parity of k is always flipped. 
    - game stops when k == 0, there are no more "U"
    - 
    - for odd k to become 0 (even), takes odd steps, alice always has a move
    """

    count = s.count("U")
    return True if count % 2 != 0 else False

for _ in range(int(input())):
    n = int(input())
    s = list(input())
    print("YES" if solve(s) else "NO")

