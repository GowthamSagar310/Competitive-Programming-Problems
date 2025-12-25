for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    even_sum = sum(filter(lambda x: x % 2 == 0, arr))
    if even_sum > total - even_sum:
        print("YES")
    else:
        print("NO")