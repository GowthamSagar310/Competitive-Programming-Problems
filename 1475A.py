for _ in range(int(input())):
    n = int(input())
    # print("YES" if n.bit_count() > 1 else "NO")
    if n & (n-1):
        print("YES")
    else:
        print("NO")