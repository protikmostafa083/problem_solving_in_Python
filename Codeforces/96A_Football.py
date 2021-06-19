player = input()
player = sorted(player)
count = 0
for i in range(len(player)):
    if i == len(player)-1:
        break
    if player[i]==player[i+1]:
        count = count+1
if count>=7:
    print('YES')
else:
    print('NO')