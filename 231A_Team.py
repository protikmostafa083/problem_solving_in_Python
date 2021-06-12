rotation = int(input())
count = 0
for i in range(rotation):
    num = list(map(int, input().split()))
    if sum(num)>=2:
        count = count+1

print(count)