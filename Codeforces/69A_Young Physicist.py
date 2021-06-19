rotation = int(input())
vector = []
for i in range(rotation):
    force = list(map(int, input().split()))
    vector.append(force)
x = 0
y = 0
z = 0
for i in range(rotation):
    for j in range(rotation):
    #for x co-ordinate
        if j ==0:
            x = vector[i][j]+x
    # for x co-ordinate
        if j == 1:
            y = vector[i][j] + y
    # for x co-ordinate
        if j == 2:
            z = vector[i][j] + z
if x==0 and y==0 and z==0:
    print('YES')
else:
    print('NO')