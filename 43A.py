n = int(input())
scores = {}
maxi = 0
winner = ""
for _ in range(n):
    team = input()
    scores[team] = scores.get(team, 0) + 1
    if scores[team] > maxi:
        winner = team
        maxi = scores[team]
print(winner)