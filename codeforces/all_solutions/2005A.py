for _ in range(int(input())):
    n = int(input())

    # length of the string = n
    # a, e, i, o, u

    # string with minimal palindromic subsequences

    # a
    # ae
    # aei
    # aeio
    # aaeiou
    # aaeiouu

    # aeiou
    # vowels = ['a', 'e', 'i', 'o', 'u']
    # if n < 6:
    #     print("".join(vowels[:n]))
    # else:
    #     q = n // 5
    #     r = n % 5

    #     WRONG
    #     print("a" * (q+r) + "e" * q + "i" * q + "o" * q + "u" * q)


    # "aaa" if there are "k" a's, we have (2^k)-1 subsequences
    # and each subsequence is a palindrome anyway
    # why (2^k)-1 ? 
    # think in terms of recursion to build subsequnces
    # first character can be included or can be left out - 2 choices
    # same with all characters
    # 2 * 2 * 2 possbilities
    # but we are removing empty subsequences (where non of the chars are choosen)
    # (2^k)-1

    # in the above logic, "a" is repeated (q+r) times
    # meaning (2^(q+r))-1
    # but it is better have q+r distributed across characters, to make the above value less
    # instead of having 2^4, it is better to have 2^2 + 2^2 

    vowels = ['a', 'e', 'i', 'o', 'u']
    q = n // 5
    r = n % 5
    res = []
    for i in range(5):
        if i < r:
            count = q + 1
        else:
            count = q
        res.append(vowels[i] * count)
    print("".join(res))    
