n, k = map(int, input().split())
s = input()

# which side to go first ? 
# k vs n-k

left_distance = k-1
right_distance = n-k

if left_distance <= right_distance:
    for _ in range(left_distance): print("LEFT")
    for i in range(n):
        print(f"PRINT {s[i]}")
        if i < n - 1:
            print("RIGHT")
else:
    for _ in range(right_distance): print("RIGHT")
    for i in range(n - 1, -1, -1):
        print(f"PRINT {s[i]}")
        if i > 0:
            print("LEFT")