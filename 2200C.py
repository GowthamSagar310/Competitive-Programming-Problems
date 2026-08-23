for _ in range(int(input())):
    n = int(input())
    s = input()
    stack = []
    for i in range(n):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    print("YES" if not stack else "NO")