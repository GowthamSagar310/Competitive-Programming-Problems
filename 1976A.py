for _ in range(int(input())):
    n = int(input())
    s = input()

    # no number after letter
    # all numbers are in non-decreasing order
    # all letters are sorted in non-decreasing order

    prev_letter = prev_num = None
    for i,l in enumerate(s):
        if l.isalpha():
            if prev_letter:
                if l < prev_letter:
                    print("NO")
                    break
            prev_letter = l
        elif l.isdigit():
            if i-1 >= 0 and s[i-1].isalpha():
                print("NO")
                break
            if prev_num:
                if int(l) < prev_num:
                    print("NO")
                    break
            prev_num = int(l)
    else:
        print("YES")
                    
