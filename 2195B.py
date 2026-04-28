def in_gp(i1, i2):

    if i1 < i2: i1, i2 = i2, i1
    """
    GP = i, 2i, 4i, 8i, ...

    kth term = a * 2^k
    i1 = a * 2^k1
    i2 = a * 2^k2

    i1/ i2 is always power of 2 (i1 >= i2)
    """

    if i1 % i2 != 0: return False
    r = i1 // i2
    return r > 0 and (r & (r-1)) == 0

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    def solve(arr, n):
        
        m = {val: index+1 for index, val in enumerate(arr)}

        for i in range(n):
            if i+1 != arr[i]:
                # somehow we need to swap this with other elements
                # actual index of element which should be here = m[i+1]
                # current index = i
                # are these in a GP sequence
                # i, 2i, 4i, 8i etc. ?
                # if they are we can swap them.

                # one based
                curr_index = i+1
                required_index = m[i+1]

                if not in_gp(required_index, curr_index):
                    return False

        return True 
    print("YES" if solve(arr, n) else "NO")