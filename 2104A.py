for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if (a + b + c) % 3 == 0:
        avg = (a + b + c) // 3
        if a > avg or b > avg:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")
