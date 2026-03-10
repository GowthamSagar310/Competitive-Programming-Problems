n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

def or_val(arr):
    value = 0
    for val in arr:
        value |= val
    return value

print(or_val(arr1) + or_val(arr2))