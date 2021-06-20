number = int(input())
possibilities = [4, 7, 44, 47, 74, 77, 444, 474, 447, 477, 744, 747, 774, 777]
flag = 0
for i in range(len(possibilities)):
    if number % possibilities[i] == 0:
        flag = 1
print('YES') if flag == 1 else print('NO')
