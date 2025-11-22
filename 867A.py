n = int(input())
s = input()

# prev = s[0]
# s_to_f = f_to_s = 0
# for i in range(1, n):
#     if prev == "S" and s[i] == "F":
#         s_to_f += 1
#     if prev == "F" and s[i] == "S":
#         f_to_s += 1
#     prev = s[i]
# print("YES" if s_to_f > f_to_s else "NO")

# if the starting position is "S", the change is going to increase s_to_f += 1
# the next following can be "S" or "F", meaning "SFS" or "SFF"
# if the end is S, we are going to increase f_to_s += 1, which makes s_to_f, f_to_s equal
# if the end is F, we are either going to increase s_to_f += 1 or not,
# which keeps s_to_f bigger, as we started with it
print("YES" if s[0] == "S" and s[-1] == "F" else "NO")

# "FFFSSSS" -> NO
# "SSSSFSFSFF"


# Every time you switch S → F, at some later point (unless the string ends there) you must eventually switch back with F → S
# Thus, s_to_f and f_to_s differ by at most 1.

# who gets the lead ? 
# 1. if it starts with S, ends with F, s_to_f has the lead
# 2. if it starts with F, ends with S, f_to_s has the lead
# 3, if is starts and ends with S or F, s_to_f == f_to_s