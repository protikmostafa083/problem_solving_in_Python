n = int(input())
vol =  list(map(int, input().split()))
percentage = 0
for i in range(n):
    percentage = percentage + vol[i]/100
print((percentage/n)*100)