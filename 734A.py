n = int(input())
s = input()
a_count = s.count("A")
b_count = n - a_count
if a_count == b_count:
    print("Friendship")
elif a_count < b_count:
    print("Danik")
else:
    print("Anton")