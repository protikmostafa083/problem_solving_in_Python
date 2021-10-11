testcases = int(input())
for i in range(testcases):
    a, b = map(int, input().split())
    if a == b:
        print((a + b) ** 2)
    elif a > 2 * b or b > 2 * a:
        print(max(a, b) ** 2)
    elif (b < a <= 2 * b) or (a < b <= 2 * a):
        print((min(a, b) * 2) ** 2)
