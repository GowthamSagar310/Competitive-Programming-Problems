"""
- he needs to eat all the piles of food. 



- if median value is choosen to the initial v ? 

3 10 9 8 7

"""


for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    # consecutive groups of numbers.
    # as long as there is over lap, it works. 

    count = 0
    mini = maxi = arr[0]
    for i in range(1, n):
        mini, maxi = min(mini, arr[i]), max(maxi, arr[i])
        l1, r1 = mini-x, mini+x
        l2, r2 = maxi-x, maxi+x
        if l2 > r1:
            count += 1
            mini = maxi = arr[i]
    print(count)