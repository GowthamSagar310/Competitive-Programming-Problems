def move_pointer(pointer):
    while pointer >= 0 and present[pointer] != 0:
        pointer -= 1
    return pointer

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    present = [0] * (n+1)
    for i in range(n):
        if arr[i] != 0:
            present[arr[i]] = 1

    pointer = n
    pointer = move_pointer(pointer)
    if pointer == -1: print(0); continue
    
    misplaced = [-1, -1]
    for i in range(n):
        if arr[i] == 0:
            arr[i] = pointer
            present[arr[i]] = 1
            pointer = move_pointer(pointer)
        if arr[i] != i+1:
            if misplaced[0] == -1:
                misplaced[0] = i
            else:
                misplaced[1] = i
    print(misplaced[1]-misplaced[0]+1 if misplaced[0] != -1 else 0)