rot = int(input())
height = list(map(int, input().split()))
minElem = min(height)
maxElem = max(height)
minElemIndex = 0
maxElemIndex = rot
for i in range(rot):
    if height[i] == minElem:
        if i > minElemIndex:
            minElemIndex = i
    if height[i] == maxElem:
        if i < maxElemIndex:
            maxElemIndex = i
if maxElemIndex>minElemIndex:
    print(abs(0 - maxElemIndex) + abs((rot - 1) - (minElemIndex + 1)))
else:
    print(abs(0-maxElemIndex)+abs((rot-1)-minElemIndex))
