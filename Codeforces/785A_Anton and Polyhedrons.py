test_case = int(input())
ans = 0
for i in range(test_case):
    inp = input()
    if inp == 'Tetrahedron':
        ans += 4
    if inp == 'Cube':
        ans += 6
    if inp == 'Octahedron':
        ans += 8
    if inp == 'Dodecahedron':
        ans += 12
    if inp == 'Icosahedron':
        ans += 20
print(ans)
