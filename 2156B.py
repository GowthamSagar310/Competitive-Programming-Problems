for _ in range(int(input())):
    n, q_len = map(int, input().split())
    s = input()
    queries = list(map(int, input().split()))

    """
    - how many ops ?
        - but if everything is type A, it would take O(number) = O(10^9)
        - if there are no Bs, that means, the decrease per cycle is constant. 
        - we should be able to calculate this. 

        - but if everything is type B, it would take log2(10**9) ~ log2(2^30) ~30
        - even if there is atleast one B, then it would take only < 30 steps
        

    - there are 20 machines
    - 10^4 queries * 30 ops 
    """
    count_b = s.count("B")
    for a in queries:
        if count_b:
            ops = 0
            i = 0
            while a != 0:
                if s[i] == "A": a -= 1
                else: a //= 2
                i = (i + 1) % n
                ops += 1
            print(ops)            
        else:
            print(a)
