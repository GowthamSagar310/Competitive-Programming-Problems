n = int(input())
if n <= 2:
    print(-1)
else:
    print("2 3 1 " + " ".join(["3"] * (n-3)))