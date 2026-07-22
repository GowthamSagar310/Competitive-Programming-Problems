for _ in range(int(input())):
    n = int(input())
    s = input()
    indices = [i+1 for i in range(n) if s[i] == '0']
    print(len(indices))
    print(*indices)