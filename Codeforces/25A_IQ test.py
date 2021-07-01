# Problem Statement
'''
Here, the objective is to find out when the flow breaks.
let's say we have a number flow of all even number but there is one teeny tiny odd :')
or vice versa!
we need to find out the index of that teeny tiny culprit who is breaking the order.
and the following code does the BAM!s
'''
amount = int(input())
numbers = list(map(int, input().split()))
countEven, countOdd = 0, 0
indexEven, indexOdd = 0,0
for i in range(amount):
    if numbers[i]%2==0:
        countEven+=1
        indexEven=i
    if numbers[i]%2!=0:
        countOdd+=1
        indexOdd=i
if countEven>countOdd:
    print(indexOdd+1)
else:
    print(indexEven+1)