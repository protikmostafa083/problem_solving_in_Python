n = int(input())
peeps = list(map(str, input().split()))
taxi, c4, c3, c2, c1 = 0, 0, 0, 0, 0
for i in range(n):
    if '4' in peeps[i]:
        c4 += 1
    if '3' in peeps[i]:
        c3 += 1
    if '2' in peeps[i]:
        c2 += 1
    if '1' in peeps[i]:
        c1 += 1
taxi = c4
if c1 != 0 and c3 != 0:
    if c3==c1:
        taxi = taxi + c1
        c3 = 0
        c1 = 0
    if c3>c1:
        taxi = taxi + c1
        c3 = c3 - c1
        c1 = 0
    if c1>c3:
        taxi = taxi + c3
        c1 = c1 - c3
        c3 = 0
if c3 != 0 and c1 == 0:
    taxi = taxi + c3
    c3 = 0
if c2 % 2 == 0:
    taxi = taxi + int(c2 // 2)
    c2 = 0
if c2 % 2 != 0:
    taxi = taxi + int(c2 // 2)
    c2 = 1
if c2 == 1:
    if c1 <= 2:
        c1 = 0
        c2 = 0
        taxi = taxi + 1
    if c1 > 2:
        c1 = c1 - 2
        c2 = 0
        taxi = taxi + 1
if c1 != 0:
    taxi = taxi + (c1 // 4)
    if c1 % 4 != 0:
        taxi = taxi + 1
        c1 = 0

print(taxi)
