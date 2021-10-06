col, row = map(int, input().split())
flag = 0
for i in range(1, col + 1):
    if i % 2 == 1:
        print(row * '#')
    elif i % 2 == 0 and flag == 0:
        print((row - 1) * '.' + '#')
        flag = 1
    elif i % 2 == 0 and flag == 1:
        print('#' + (row - 1) * '.')
        flag = 0
