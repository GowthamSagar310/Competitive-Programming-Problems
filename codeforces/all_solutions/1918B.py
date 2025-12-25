for _ in range(int(input())):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    res1, res2 = [], []

    for a, b in sorted([(a, b) for a, b in zip(arr1, arr2)]):
        res1.append(str(a))
        res2.append(str(b))
    
    print(" ".join(res1))
    print(" ".join(res2))