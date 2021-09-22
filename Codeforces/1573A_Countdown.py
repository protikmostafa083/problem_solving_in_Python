# Declaring the number of testcases
test = int(input())
for i in range(test):
    steps = 0
    n = int(input())
    vals = int(input())
    vals = [int(val) for val in str(vals)]
    steps = sum(vals)
    vals = list(map(str, vals))
    for j in range(len(vals) - 1):
        if vals[j] != '0':
            steps += 1
    print(steps)
