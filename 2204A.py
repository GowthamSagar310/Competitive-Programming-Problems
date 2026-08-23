for _ in range(int(input())):
    n = int(input())
    s = input()
    index = s.find("RL")
    print(index+2 if index != -1 else n)