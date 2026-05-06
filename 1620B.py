for _ in range(int(input())):
    w, h = map(int, input().split())

    # horizontal
    b_max = 0
    for _ in range(2):
        k, *arr = map(int, input().split())
        b_max = max(b_max, arr[-1]-arr[0])
    
    # vertical
    h_max = 0
    for _ in range(2):
        k, *arr = map(int, input().split())
        h_max = max(h_max, arr[-1]-arr[0])
    
    print(max(b_max * h, h_max * w))
