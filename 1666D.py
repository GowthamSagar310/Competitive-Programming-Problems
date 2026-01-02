# for _ in range(int(input())):
#     s, t = input().split()
#     ns, nt = len(s), len(t)
#     i, j = ns-1, nt-1
#     all_deleted = set()
#     while i >= 0 and  j >= 0:
#         if s[i] == t[j] and s[i] not in all_deleted:
#             i -= 1
#             j -= 1
#         else:
#             while i >= 0 and (s[i] != t[j] or s[i] in all_deleted):
#                 all_deleted.add(s[i])
#                 i -= 1
    
#     print("YES" if j == -1 else "NO")


# simpler implementation
for _ in range(int(input())):
    s, t = input().split()
    ns, nt = len(s), len(t)
    i, j = ns-1, nt-1
    all_deleted = set()
    while i >= 0 and  j >= 0:
        if s[i] == t[j]:
            if s[i] in all_deleted:
                i -= 1
            else:
                i -= 1
                j -= 1
        else:
            all_deleted.add(s[i])
            i -= 1
    print("YES" if j == -1 else "NO")