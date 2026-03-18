n = int(input())
arr = list(map(int, input().split()))

even = list(filter(lambda x: x % 2 == 0, arr))
odd = list(filter(lambda x: x & 1, arr))

if abs(len(even)-len(odd)) <= 1:
    print(0)
else:
    if len(even) > len(odd):
        even.sort()
        diff = len(even)-len(odd)
        print(sum(even[:diff-1]))
    else:
        odd.sort()
        diff = len(odd)-len(even)
        print(sum(odd[:diff-1]))