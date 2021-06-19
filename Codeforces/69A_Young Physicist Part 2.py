rotataion = int(input())
x, y, z = 0, 0, 0
for i in range(rotataion):
    #for X axis
    inx, iny, inz = map(int, input().split())
    x = inx + x
    y = iny + y
    z = inz + z
if x==0 and y==0 and z==0:
    print('YES')
else:
    print('NO')