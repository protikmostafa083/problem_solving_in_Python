candidates,cutposition = map(int,input().split())
a = list(map(int, input().split()))
count = 0
for i  in range(len(a)):
    if a[i]>0 and a[i]>=a[cutposition-1]:
        count = count+1
print(count)