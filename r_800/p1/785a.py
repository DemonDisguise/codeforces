n = int(input())
shapes = {"Tetrahedron": 4, "Cube": 6, "Octahedron": 8, "Dodecahedron": 12, "Icosahedron": 20}
print(sum(shapes[input()] for _ in range(n)))
