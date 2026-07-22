for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    """
    - cost of the string = length of longest subsequence that is a bracket sequence.
    - remove atmost "k" characters from string "s", so that the cost of the resulting string is minimized. 
    """

    def recur(i, k_left):

            
        # remove the character
        if k_left > 0:
            recur(i+1, k_left-1, open_brackets)