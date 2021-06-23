rot = int(input())
count  = 0
for i in range(rot):
    currentResident, capacity = map(int, input().split())
    if currentResident<=capacity-2:
        count+=1
print(count)