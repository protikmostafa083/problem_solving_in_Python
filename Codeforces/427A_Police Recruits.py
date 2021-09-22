test = int(input())
situations = list(map(int, input().split()))
cntPos, cnt = 0, 0
for situation in situations:
    if situation < 1 and cntPos == 0:
        cnt += 1
    elif situation < 1 and cntPos > 0:
        cntPos -= 1
    elif situation > 0:
        cntPos += situation
print(cnt)
