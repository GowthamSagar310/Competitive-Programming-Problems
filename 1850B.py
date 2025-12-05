for _ in range(int(input())):
    n = int(input())
    maxi = 0
    ans = 0
    for i in range(n):
        length, quality = map(int, input().split())
        if length <= 10:
            if quality > maxi:
                maxi = quality 
                ans = i+1
    print(ans)