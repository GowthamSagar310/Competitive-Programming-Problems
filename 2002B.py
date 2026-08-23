for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # l1, r1 = 0, n-1
    # l2, r2 = 0, n-1
    # alice_wins = False
    # for i in range(n):
    #     a_f, a_l = a[l1], a[r1]
    #     b_f, b_l = b[l2], b[r2]
    #     if a_f not in [b_f, b_l] or a_l not in [b_f, b_l]:
    #         alice_wins = True
    #         break
    #     else:
    #         if a_f == b_f: l1 += 1; l2 += 1
    #         elif a_f == b_l: l1 += 1; r2 -= 1
    #         elif a_l == b_f: r1 -= 1; l2 += 1
    #         else: r1 -= 1; r2 -= 1
    # print("Alice" if alice_wins else "Bob")

    """
    - the idea here is when can bob cannot make it equal with the alice ? 
    - lets there is a subarray in "a", if it is not present in "b" as a subarray too (same length)
    - for example [1, 2, 4, 3, 5] [1, 2, 5, 4, 3]
    - alice has [2, 4] but that is not part of bob's array
    - [2, 4]  (after removing three elements)
    - [4, 3] [1, 2] [5, 4], [2, 5] (bob can have these combinations)
    - none of this work in bob's favour because alice can always keep the element which is not present in the bob's arrays
    - 

    - the idea here is that if alice has a contiguous array of elements which bob does not have,
    - alice can keep that and force the bob to remove one of the element which is present in alice's sub array
    - the element which is forced, can be kept by alice till the end to force a win. 

    - alice cannot do it, only when there is no such contiguous array
    - which is same array for alice and bob and also reverse.
    """

    if a == b or a == b[::-1]:
        print("Bob")
    else:
        print("Alice")