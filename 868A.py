s = input()
n = int(input())
barks = []
for _ in range(n):
    b = input()
    barks.append(b)

def solve(s, barks):
    first_letter = []
    second_letter = []
    for b in barks:
        if b == s:
            return True
        if b[1] == s[0]:
            first_letter.append(b)
        if b[0] == s[1]:
            second_letter.append(b)
    
    if first_letter and second_letter:
        return True
    return False
    
print("YES" if solve(s, barks) else 'NO')