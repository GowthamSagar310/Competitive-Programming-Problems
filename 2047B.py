from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    s = list(input())

    # replace the most repeated character with the least repeated character

    freq = defaultdict(int)
    for l in s: freq[l] += 1
    values = sorted(freq.items(), key= lambda x: x[1])

    most_repeated_char = values[-1][0]
    least_repeated_char = values[0][0]

    for i, l in enumerate(s):
        if l == least_repeated_char:
            s[i] = most_repeated_char
            break
    
    print("".join(s))
