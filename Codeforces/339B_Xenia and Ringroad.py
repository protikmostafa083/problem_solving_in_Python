houseNum, taskHouse = map(int, input().split())
initPos = 1
tasks = list(map(int, input().split()))
move = 0
for i in range(taskHouse):
    if initPos==tasks[i]:
        continue
    elif initPos>tasks[i]:
        move = move + (houseNum-initPos) + tasks[i]
        initPos = tasks[i]
    else:
        move = move + (tasks[i] - initPos)
        initPos = tasks[i]

print(move)