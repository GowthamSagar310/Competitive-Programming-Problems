from collections import Counter

n = int(input())
s = Counter(input())

# z e r o -> z, r are unique to zero
# o n e -> n is unique to one

zeros_count = s["z"] if "z" in s else 0
ones_count = s["n"] if "n" in s else 0
print("1 " * ones_count + "0 " * zeros_count)