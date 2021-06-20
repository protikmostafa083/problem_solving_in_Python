stunum, time = map(int, input().split())
stupos = list(input())
for i in range(time):
    j = 0
    while(j<stunum-1):
        if stupos[j] == 'B' and stupos[j + 1] == 'G':
            stupos[j] = 'G'
            stupos[j + 1] = 'B'
            j = j + 2
        else:
            j = j + 1

print("".join(stupos))