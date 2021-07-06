shocksStock, dayInterval = map(int, input().split())
day = 0
while shocksStock > 0:
    day += 1
    shocksStock -= 1
    if day % dayInterval == 0:
        shocksStock += 1
print(day)
