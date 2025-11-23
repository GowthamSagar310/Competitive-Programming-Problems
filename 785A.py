faces = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}

res = 0
for _ in range(int(input())):
    p = input()
    res += faces[p]
print(res)