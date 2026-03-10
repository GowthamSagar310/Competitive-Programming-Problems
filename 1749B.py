for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # all the monsters are to be killed -> so sum(a) will always be part of ans
    # if the monster is in middle (that has left and right neighbours) -> 2 * bi
    # if at the ends it will add -> bi
    # (so atleast bi is added)

    # last monster is not going to add anything.
    
    # for a given last monster, we can always choose the ends of the array
    # so that bi is added only once
    # is index "x" is choosen
    # 1 2 3 4 ... x-1, and then n, n-1, .... x+1
    # can be choosen to add bi to the ans

    print(sum(a) + sum(b) - max(b))