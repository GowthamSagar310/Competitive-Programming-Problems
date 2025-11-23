s = input()

# a, b, c, d, ........ z
# 0, 1, 2, 3, ........ 25

# it takes 26 turns to come to the same position (full circle)
# so in one direction, if it takes k steps to reach, from the opposite it would take 26-k
# just have to minimum of it. 


current_letter = "a"
rotations = 0
for l in s:
    k = abs(ord(l)-ord(current_letter))
    rotations += min(k, 26-k)
    current_letter = l
print(rotations)