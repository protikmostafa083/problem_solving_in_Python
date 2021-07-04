rot = int(input())
group = 1
prevElem = int(input())
for i in range(1,rot):
    newElem = int(input())
    if newElem != prevElem:
        prevElem = newElem
        group +=1
print(group)