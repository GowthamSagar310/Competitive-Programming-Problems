# values = {
#     "A": +1,
#     "B": 0,
#     "C": -1,
#     "?": 0,
#     1: "A",
#     0: "B",
#     -1: "C"
# }

# for _ in range(int(input())):
#     matrix = []
#     for _ in range(3):
#         matrix.append(input())

#     for r in range(3):
#         row = matrix[r]
#         if "?" in row:
#             print(values[-1 * sum(map(lambda x: values[x], row))])
#             break

# bitwise solution
# think about a, b, c in terms of some number
# a = 1 
# b = 2 
# c = 3 
# (we can take any numbers, but this is simpler)

# a ^ b ^ c ^ a ^ b -> c (missing)
# similarily, we can get odd one 



values = {
    "A": 1,
    "B": 2,
    "C": 3,
    1: "A",
    2: "B",
    3: "C"
}

q_index = -1
for _ in range(int(input())):
    matrix = []
    xor = 1 ^ 2 ^ 3
    for i in range(3):
        row = input()
        if "?" in row:
            q_index = i
        matrix.append(row)
    
    for l in matrix[q_index]:
        if l == "?":
            continue
        xor = xor ^  values[l]
    
    print(values[xor])