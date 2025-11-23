first = {l: index for index, l in enumerate(input())}
second = input()

res = []
typed = input()
for l in typed:
    if l.isdigit():
        res.append(l)
    else:
        first_index = first[l.lower()]
        second_letter = second[first_index]
        res.append(second_letter if l.islower() else second_letter.upper())
print("".join(res))