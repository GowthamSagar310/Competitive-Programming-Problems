scores = list(map(int, input().split()))
scores.sort()

if scores[-1]-scores[0] >= 10:
    print("check again")
else:
    print("final " + str(scores[1]))


