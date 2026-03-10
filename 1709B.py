n, m = map(int, input().split())
arr = list(map(int, input().split()))

pre = [0] * n
suf = [0] * n
for i in range(n-1):
    if arr[i] > arr[i+1]:
        pre[i+1] = pre[i] + arr[i]-arr[i+1]
    else:
        pre[i+1] = pre[i]
        

for i in range(n-2, -1, -1):
    if arr[i] < arr[i+1]:
        suf[i] = suf[i+1] + arr[i+1]-arr[i]
    else:
        suf[i] = suf[i+1]

for _ in range(m):
    s, t = map(int, input().split())
    if s < t:
        print(pre[t-1]-pre[s-1])
    else:
        print(suf[t-1]-suf[s-1])

