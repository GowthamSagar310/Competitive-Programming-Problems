n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()


"""

20 30 40


0   1  2  3 4   5       
20 20 40 50 50 100



4 = 5-l+1
l = 5-4+1
l = n-k+1


"""

print(arr[n-k])