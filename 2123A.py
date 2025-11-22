# 0 1 2 3 4 5 ... n-1
# choose integer a 
# choose integer b such that (a + b) % 4 = 3

# n = 2
# 0 1
# no matter what number is choosen, alice always wins 

# n = 4
# 0 1 2 3
# a = 0, b = 3
# a = 1, b = 2
# a = 2, b = 1
# b = 3, b = 0

# n = 5
# 0 1 2 3 4
# a = 0, b = 3
# a = 1, b = 2
# a = 4, b ?

for _ in range(int(input())):
    n = int(input())
    if n-1 > 4:
        print("Alice")
    