for _ in range(int(input())):
    n = int(input())
    s = input()
    print(max(ord(l)-ord('a')+1 for l in s))