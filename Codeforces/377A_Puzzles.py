wannaBuy, shopsells = map(int, input().split())
sellList = list(map(int, input().split()))
sellList.sort()
minDiff = []
for i in range(shopsells-wannaBuy + 1):
    diffObtained =  sellList[i+wannaBuy-1] - sellList[i]
    minDiff.append(diffObtained)
print(min(minDiff))