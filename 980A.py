s = input()
pearls = s.count("o")
links = len(s)-pearls
if not pearls or links % pearls == 0:
    print("YES")
else:
    print("NO")