a = input()
b = input()

def solve(a, b):
    n1, n2 = len(a), len(b)
    i = 0
    while i < n1 and a[i] == '0': i += 1
    j = 0
    while j < n2 and b[j] == '0': j += 1
    if n1-i+1 > n2-j+1:
        return ">"
    elif n1-i+1 < n2-j+1:
        return "<"
    else:
        while i < n1:
            if a[i] < b[j]:
                return "<"
            elif a[i] > b[j]:
                return ">"
            i += 1
            j += 1
        return "="

print(solve(a, b))