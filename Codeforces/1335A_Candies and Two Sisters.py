testCase = int(input())
for i in range(testCase):
    num = int(input())
    if num<3:
        print(0)
        continue
    if num%2==0:
        print(int(num/2)-1)
    else:
        print(int(num/2))