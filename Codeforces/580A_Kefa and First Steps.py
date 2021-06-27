n = int(input())
num = list(map(int, input().split()))
count, highest = 0, 0
for i in range(n-1):
    if num[i]<=num[i+1]:
        count += 1
    else:
        count = count
    if count>highest:
        highest = count
    if num[i]>num[i+1]:
        count =0
print(highest+1)