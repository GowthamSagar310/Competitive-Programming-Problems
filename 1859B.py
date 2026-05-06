for _ in range(int(input())):
    n = int(input())
    arrays = []
    seconds = []
    minimum = float("inf")
    for _ in range(n):
        l = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        minimum = min(minimum, arr[0])
        seconds.append(arr[1])
    
    seconds.sort(reverse=True)
    beauty = sum(seconds[:-1])
    beauty += minimum
    print(beauty)


