# this is a very good problem
# this is an excellent idea on calculating digit sums from 1 to n
# instead of computing this for each test case, we compute only once.


MAX_N = 200000
digit_sums = [0] * (MAX_N+1)
ans = [0] * (MAX_N+1)
for i in range(1, MAX_N+1):
    digit_sums[i] = digit_sums[i//10] + (i%10)
    ans[i] = ans[i-1] + digit_sums[i]

for _ in range(int(input())):
    n = int(input())
    print(ans[n])    
