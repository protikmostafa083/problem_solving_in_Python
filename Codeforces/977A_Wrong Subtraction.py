innum, step = map(int, input().split())
modnum = innum
for i in range(step):
    if modnum%10==0:
        modnum = modnum/10
    else:
        modnum = modnum-1
print(int(modnum))