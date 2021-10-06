numberOfTasks, timeToReachParty = map(int, input().split())
spareTime = 240 - timeToReachParty
for i in range(1, numberOfTasks + 1):
    spareTime = spareTime - (i * 5)
    if spareTime < 0:
        print(i - 1)
        break
    else:
        if i == numberOfTasks:
            print(i)
