n = int(input())    
arr = list(map(int, input().split()))
s = sum(arr)

if s % 2 == 0:
    print(len(list(filter(lambda x: x % 2 == 0, arr))))
else:
    print(len(list(filter(lambda x: x % 2 != 0, arr))))