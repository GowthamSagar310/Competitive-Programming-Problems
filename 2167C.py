for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    any_even = any(val % 2 == 0 for val in arr)
    any_odd = any(val % 2 != 0 for val in arr)
    if any_even and any_odd:
        print(" ".join(map(str, sorted(arr))))
    else:
        print(" ".join(map(str, arr)))
        