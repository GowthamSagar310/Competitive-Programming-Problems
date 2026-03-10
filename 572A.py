n1, n2 = map(int, input().split())
k, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

"""

any choosen number from "k" values of arr1 
should be strictly less than 
any choosen number from "m" values of arr2

meaning, max of k values < min of m values
choose the first k values of arr1
choose the last m values of arr2
"""

if arr1[k-1] < arr2[n2-1-(m-1)]:
    print("YES")
else:
    print("NO")