for _ in range(int(input())):
    n = int(input())
    s = input()

    one_count = zero_count = 0
    i = 0
    while i < n:
        if s[i] == "1":
            one_count += 1
            i += 1
        else:
            zero_count += 1
            while i < n and s[i] == "0":
                i += 1
    
    if one_count > zero_count:
        print("Yes")
    else:
        print("No")