testCase = int(input())
for i in range(testCase):
    a, b = map(int, input().split())
    if a % b != 0:
        print((int(a // b) + 1) * b - a)
    else:
        print(0)
