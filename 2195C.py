def are_opposite(x, y):
    return x == y or x == 7-y or y == 7-x

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ops = 0
    for i in range(n-1):
        if are_opposite(arr[i], arr[i+1]):
            nums = set([1, 2, 3, 4, 5, 6])
            for val in [
                arr[i],
                7-arr[i],
                arr[i+1]
            ]:
                nums.discard(val)
            if i+2 < n:
                nums.discard(arr[i+2])
                nums.discard(7-arr[i+2])
            
            arr[i+1] = list(nums)[0]
            ops += 1
    print(ops)