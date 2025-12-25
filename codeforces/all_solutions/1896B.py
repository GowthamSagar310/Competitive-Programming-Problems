for _ in range(int(input())):
    n = int(input())
    s = list(input())

    # simulation
    # marked = [0] * n
    # ops = 0
    # for i in range(n):
    #     if s[i] == "B":
    #         j = i-1
    #         while j >= 0 and s[j] == "A" and marked[j] != 1:
    #             s[j], s[j+1] = s[j+1], s[j]
    #             ops += 1
    #             marked[j] = 1
    #             j -= 1
    # print(ops)

    # the observation to make here is 
    # all the B's before the first A are useless
    # all the A's after the last B are useless
    # all the indice between the first_a and last_b
    # can be used to swap 
    # 
    # think of each index as a bridge, say k is the index
    # first_a <= k <= last_b
    # meaning there is a A on left side of k and B on the right side k
    # eventually that B is going to flow left and A is going to flow right
    # which they get swapped at k

    first_a = last_b = -1
    for i in range(n): 
        if s[i] == "A": 
            first_a = i
            break
    for i in range(n-1, -1, -1):
        if s[i] == "B":
            last_b = i
            break
    
    if first_a == -1 or last_b == -1 or first_a > last_b:
        print(0)
    else:
        print(last_b - first_a)

        # from 2nd to 6th index we can swap -> 5 -> (7-2)
        # B B A A B B A B A A A
        # 0 1 2 3 4 5 6 7 8 9 10
        #     |________ |

    # first_a = s.find("A") returns -1 if not found
    # last_b = s.rfind("B")