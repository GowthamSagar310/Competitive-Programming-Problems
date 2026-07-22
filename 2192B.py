for _ in range(int(input())):
    n = int(input())
    s = input()
    
    """
    - binary string 
    - choose index i, flip every other index
    - only once at each index
    - no need to minimize ops 
    - should convert the binary string to 0s


    - operation can be rephrased into
    - flip all the bits and then flip pth bit again
    - if the total number of operations performed is k, 
    - then all the bits will be flipped k times.
    - all the choosen bits will be flipped again k-1 times

    - by flipping k times, if i have to make the bit = 0
    - original val = 0, k should be even
    - original val = 1, k should be odd

    - by flipping k-1 times, if i have to make the bit = 0 
    - original val = 0, k-1 should be even, k should be odd
    - original val = 1, k-1 should be odd, k should be even

    Case A: k = even
    - current_bit = 0
    - to make it stay as 0, we cannot choose it. 
    - bceause we choose it, k-1 flips turns it to 1.
    - so we can only choose 1s
    - should we choose all 1s ? yes, because k is even, if 1 is unchoosen, it will still be 1.
    - if i have choose all 1s, then
    - if 1s are odd which is not equal to k even ops we assumed = we cannot have a solution. 
    - so 1s must also be even

    case B: k = odd
    - current_bit = 1
    - to make to turn into 0, we need to flip it k times
    - so we cannot choose 1, since choosen ones are flipped k-1 times
    - so we need to choose 0s. 
    - so, count of 0s must be equal = k = odd
    
    """

    zeroes = s.count("0")
    ones = n - zeroes
    if ones % 2 == 0:
        indicies = [i+1 for i in range(n) if s[i] == "1"]
        print(len(indicies))
        if indicies:
            print(*indicies)
    elif zeroes % 2 == 1:
        indicies = [i+1 for i in range(n) if s[i] == "0"]
        print(len(indicies))
        if indicies:
            print(*indicies)
    else:
        print(-1)

