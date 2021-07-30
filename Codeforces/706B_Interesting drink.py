def SearchResult(price, ability):
    lowerBound = 0
    upperBound = len(price)
    while lowerBound < upperBound:
        midRange = (lowerBound + upperBound) // 2
        if price[midRange] > ability:
            upperBound = midRange
        else:
            lowerBound = midRange + 1
    return lowerBound


shops = int(input())
price = sorted(map(int, input().split()))
daysToDrink = int(input())
for i in range(daysToDrink):
    ability = int(input())
    print(SearchResult(price, ability))
