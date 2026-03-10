n = int(input())
s = list(input())
i_to_l = {0: "A", 1: "C", 2: "G", 3: "T"}
l_to_i = {"A": 0, "C": 1, "G": 2, "T": 3}
counts = [0] * 4
for l in s:
    if l != "?":
        counts[l_to_i[l]] += 1
max_freq = n / 4
if n % 4 == 0 and max(counts) <= (n // 4):
    for i, l in enumerate(s):
        if l == "?":
            for j, val in enumerate(counts):
                if val != max_freq:
                    s[i] = i_to_l[j]
                    counts[j] += 1
                    break
    print("".join(s))
else:
    print("===")