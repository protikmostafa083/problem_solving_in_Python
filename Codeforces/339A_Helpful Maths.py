num = list(map(int, input().split('+')))
num.sort()
for i in range(len(num)):
    if(i==len(num)-1):
        print(str(num[i]))
    else:
        print(str(num[i]) + '+', end='')
