ratings = []
minimum_till_now = float("inf")
judgement = None
for _ in range(int(input())):
    before, after = map(int, input().split())
    if before != after:
        judgement = "rated"
    ratings.append((before, after))

# if before != after -> round is rated
# if I find a lesser rated guy before a bigger rated guy, round is unrated
# else we cannot determine

if judgement:
    print("rated")
else:
    minimum_till_now = ratings[0][0]
    for before, after in ratings:
        if minimum_till_now < before:
            judgement = "unrated"
            break
        minimum_till_now = min(minimum_till_now, before)

    if judgement:
        print("unrated")
    else:
        print("maybe")