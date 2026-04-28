for _ in range(int(input())):
    n = int(input())

    """

    n = even
    a -b a -b
    2a - 2b = a - b
    a - b = 0
    a = b

    1 -1 1 -1

    n = odd
    a -b a -b a
    3a - 2b = a - b
    2a = b

    -a b -a b -a
    -3a + 2b = b - a
    b = 2a

    -a 2a -a 2a a
    4a-3a = a
    2a-a = a

    -1 2 -1 2 -1 

    2 * 2 - 3 * (-1) possible
    3 * 2 - 4 * (-1) np
    4 * 2 - 5 * (-1) np

    -2 3 -2 3 -2 

    a, b
    n = 2k+1

    (k+1)*a + k*b = a + b
    ak + a + bk = a + b
    ak + bk = b
    ak = b(1-k)
    a = 1-k
    b = k

    or a = k-1 and b =-k

    is one of the solitions. 
    a != 0, b != 0 -> k != 1 so n != 3

    k >= 2 -> n >= 5 always has a solution
    """

    if n % 2 == 0:
        print("YES")
        res = [1] * n
        for i in range(0, n, 2):
            res[i] *= -1
        print(*res)
    else:
        if n >= 5:
            print("YES")
            k = (n - 1) // 2
            a = k-1
            b = -k
            is_a = True
            res = []
            for i in range(n):
                if is_a:
                    res.append(a)
                else:
                    res.append(b)
                is_a = not is_a
            print(*res)
        else:
            print("NO")