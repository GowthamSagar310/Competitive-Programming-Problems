for _ in range(int(input())):
    s = input()
    # freq = [0] * 26
    # for l in s:
    #     freq[ord(l.lower())-ord('a')] += 1
    
    # l = []
    # for i in range(25, -1, -1):
    #     l.append((chr(ord('a')+i).upper()) * freq[i])

    # print("".join(l)) 

    print("".join(sorted(s, reverse=True)))