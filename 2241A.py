for _ in range(int(input())):
    x, y = map(int, input().split())

    if x < y:
        print("NO")
    elif x == y:
        print("YES")
    else:
        # x > y case 
        if x % y == 0:
            print("YES")
        else:
            print("NO")