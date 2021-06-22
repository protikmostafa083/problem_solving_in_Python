rot = int(input())
record = []
for i in range(rot):
    name = input()
    mark = float(input())
    record.append([name, mark])

#second best mark
#sort the list, drag out the number and put it in a SET to avoid duplicacy
secondBest = sorted(set(mark for name, mark in record))[1]
print("\n".join(sorted([name for name, mark in record if mark == secondBest])))
