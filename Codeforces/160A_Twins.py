n = int(input())
coinValue = list(map(int, input().split()))
myTake = []
sumMine, sumSibling, count = 0, 0, 0
for i in range(n):
    maxVal = max(coinValue)
    myTake.append(maxVal)
    coinValue.pop(coinValue.index(maxVal))
    sumMine = sum(myTake)
    sumSibling = sum(coinValue)
    count = count + 1
    if sumMine>sumSibling:
        break
    else:
        continue
print(count)