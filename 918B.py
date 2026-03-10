mm = {}
n, m = map(int, input().split())
for _ in range(n):
    name, ip = input().split()
    mm[ip] = name

for _ in range(m):
    name, ip = input().split()
    print(f"{name} {ip} #{mm[ip[:-1]]}")