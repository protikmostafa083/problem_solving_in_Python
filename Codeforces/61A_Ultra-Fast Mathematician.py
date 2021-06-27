num1 = input()
num2 = input()
for i in range(len(num1)):
    if int(num2[i]) - int(num1[i]) != 0:
        print(1, end='')
    else:
        print(0, end='')