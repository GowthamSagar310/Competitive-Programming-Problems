for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    should_be_there = set(list(range(1, k+1)))
    for i in range(k): should_be_there.discard(arr[i])
    print(len(should_be_there))