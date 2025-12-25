for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(sum(num-min(arr) for num in arr))