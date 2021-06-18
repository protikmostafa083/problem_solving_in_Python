matrix = []         
for i in range(5):
    numbers = list(map(int,input().split()))
    matrix.append(numbers)
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            ind1 = i
            ind2 = j

move = abs(ind1-2) + abs(ind2-2)
print(move)
