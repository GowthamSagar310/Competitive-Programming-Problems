for _ in range(int(input())):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print(sum(a - b for a, b in zip(arr1, arr2) if a > b) + 1)




