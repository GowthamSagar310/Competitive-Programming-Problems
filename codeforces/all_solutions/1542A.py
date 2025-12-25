for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    even_count = sum(1 if val % 2 == 0 else 0 for val in arr)
    odd_count = 2*n - even_count
    print("Yes" if even_count == odd_count else "No")