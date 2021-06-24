rot = int(input())
numbers = list(map(int, input().split()))
for i in range(rot + 1):
    if i in numbers:
        print((numbers.index(i)) + 1, end=' ')
