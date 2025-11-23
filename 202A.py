# lexicographically largest
s = input()
max_letter = max(s, key=lambda x: ord(x))
print(max_letter * s.count(max_letter))