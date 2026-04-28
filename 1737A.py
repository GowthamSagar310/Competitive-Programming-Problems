for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())
    """
    n // k compartments. 
    
    12, 3 
    4 compartments of books. 

    cabccadabaac

    a = 5
    b = 2 
    c = 4
    d = 1

    abcd | abca | abca
    edb
    """
    freq = [0] * 26
    for l in s: freq[ord(l)-ord('a')] += 1
    res = []
    for _ in range(k):
        min_char = "a"
        steps = n // k
        for i in range(26):
            if freq[i]:
                char = chr(i + ord('a'))
                freq[i] -= 1
                if min_char == char:
                    min_char = chr(1 + ord(min_char))
                steps -= 1
                if steps == 0:
                    break
        res.append(min_char)
    print("".join(res))