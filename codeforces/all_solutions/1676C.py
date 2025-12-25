def get_difference(w1, w2):
    diff = 0
    for l1, l2 in zip(w1, w2):

        # this is not a circular array
        # so there is only one way of making the characters equal
        # 
        # forward_score ord(l2)-ord(l1)
        # backward_score ord(l1)-ord(l2)

        diff += abs(ord(l2)-ord(l1))
    return diff


for _ in range(int(input())):
    n, m = map(int, input().split())
    words = []
    for _ in range(n):
        words.append(input())
    mini = float("inf")
    for i in range(n):
        w1 = words[i]
        for j in range(i+1, n):
            w2 = words[j]
            diff = get_difference(w1, w2)
            mini = min(mini, diff)
    print(mini)