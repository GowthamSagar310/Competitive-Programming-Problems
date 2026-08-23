for _ in range(int(input())):
    n, m, k = map(int, input().split())
    missing_question_index = list(map(int, input().split()))
    known_answers = list(map(int, input().split()))

    """
    0100
    1011
    """

    if n-k > 1:
        print("0"*m)
    else:
        total = (n * (n+1)) // 2
        missing_index = total - sum(known_answers)
        ans = []
        for q in missing_question_index:
            if missing_index == 0 or q == missing_index:
                ans.append("1")
            else:
                ans.append("0")
        print("".join(ans))
