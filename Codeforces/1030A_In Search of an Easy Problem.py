n = int(input())
num = list(map(int, input().split()))
for i in range(n):
    if 1 in num:
        flag = 1
        break
    else:
        flag = 0
print('HARD') if flag == 1 else print('EASY')