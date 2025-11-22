n = int(input())


# f(n) = -1 + -3 + -5 + ... + 2 + 4 + 6 + ..

# if n is even
# same number of terms = n/2 odd + n/2 even
# 2 + 4 + 6 ... = N * (N+1)
# 1 + 3 + 5 ... = N * N

num_even = n // 2
num_odd = (n // 2) + 1 if n & 1 else n // 2
print(num_even * (num_even + 1) - (num_odd * num_odd))