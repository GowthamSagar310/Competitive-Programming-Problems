n = int(input())
arr = list(map(int, input().split()))

# ai -> for index i -> ai person gave the gift

# 2 3 4 1 
# person 1 gave gift to -> person 2  
# person 2 gave gift to -> person 3  
# person 3 gave gift to -> person 4  
# person 4 gave gift to -> person 1  

# for person 1 -> 4
# for person 2 -> 1
# for person 3 -> 2
# for person 4 -> 3

res = [0] * n
for i in range(n):

    # person (i + 1) gave gift to arr[i]
    # arr[i] recevived gift by person (i + 1)
    # res[arr[i]-1] recevied gift by person (i+1)

    res[arr[i]-1] = (i+1)
print(*res)