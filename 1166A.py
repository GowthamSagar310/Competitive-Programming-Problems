def ncr(n, r):
    if r < 0 or r > n: return 0
    if r == 0 or r == n: return 1
    ans = 1
    for i in range(r):
        ans *= n-i
        ans //= (i+1)
    return ans

n = int(input())
freq = [0] * 26
for _ in range(n): 
    name = input()
    freq[ord(name[0])-ord('a')] += 1

total = 0
for val in freq:
    if val > 2:

        # 4c2 = 6
        # 2c2 = 1, 2c2 = 1
        
        # 5c2 = 120 / 12 = 10
        # 3c2 = 3, 2c2 = 1 = 4

        odd_half = val // 2 + (1 if val & 1 else 0)
        even_half = val // 2

        total += ncr(odd_half, 2) + ncr(even_half, 2)
print(total)