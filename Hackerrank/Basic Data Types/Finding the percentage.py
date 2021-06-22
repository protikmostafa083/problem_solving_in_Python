rot = int(input())
# need a python dictionary
record = {}
for i in range(rot):
    # from the * point, it is going to create a new line and make all the variable separate.
    # here, after the name parameter is put, it is going to separate the other inputs and later on, put on a list
    name, *marks = input().split()
    marks = list(map(float, marks))
    record[name] = marks
query_name = input()
outmark = record[query_name]
print('{:.2f}'.format(sum(outmark)/len(outmark)))
