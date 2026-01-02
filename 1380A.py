# def solve(arr, n):
#     m = {} # num: index
#     for i, val in enumerate(arr): m[val] = i
#     for num in range(n, 1, -1):
#         index = m[num]
#         if index == 0 or index == n-1:
#             continue
    #     if arr[index-1] < arr[index] > arr[index+1]:
    #         print("YES")
    #         print(f"{index} {index+1} {index+2}")
    #         return
    # print("NO")
#     return

def solve(arr, n):
    for i in range(1, n-1):
        if arr[i-1] < arr[i] > arr[i+1]:
            print("YES")
            print(f"{i} {i+1} {i+2}")
            return
    print("NO")
        
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    solve(arr, n)
