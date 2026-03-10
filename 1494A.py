# def solve(s):

#     if s[0] == s[-1]:
#         return False
#     else:
#         # it might be possible
#         m = {
#             s[0]: +1,
#             s[-1]: -1
#         }

#         # the remaining character must be either ")" or "("
#         # case 1: "("
#         count = 0
#         not_ok = False
#         for i in range(len(s)):
#                 count += m.get(s[i], +1)
#                 if count < 0:
#                     not_ok = True
#                     break
#         if not not_ok and count == 0: return True

#         # case 2: ")"
#         count = 0
#         not_ok = False
#         for i in range(len(s)):
#                 count += m.get(s[i], -1)
#                 if count < 0:
#                     not_ok = True
#                     break
#         if not not_ok and count == 0: return True
        
#         return False


# simpler and trickier
def solve2(s):

    # observations
    # first and last cannot be same because first must be opening and last must be closing
    # there are always n//2 open and n//2 close brackets

    m = [0] * 3
    x = ord(s[0])-ord('A')
    y = ord(s[-1])-ord('A')
    if x == y:
        # first and last characters are same.
        return False

    m[x] = 1
    m[y] = -1
    if s.count(chr(ord('A') + x)) == len(s) // 2:
        # if the count of s[0] is n//2
        # that means the remaining charcter should be -1 as s[0] is already n//2
        m[3 ^ x ^ y] = -1
    else:
        m[3 ^ x ^ y] = 1
    
    count = 0
    for i in range(len(s)):
        count += m[ord(s[i])-ord('A')]
        if count < 0:
            return False
    return count == 0


for _ in range(int(input())):
    s = input()
    print("YES" if solve2(s) else "NO")    

