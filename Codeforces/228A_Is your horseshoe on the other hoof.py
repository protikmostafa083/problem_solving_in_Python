shoe = list(map(int, input().split()))
stand = []
for i in range(4):
    if shoe[i] not in stand:
        stand.append(shoe[i])
print(4-len(stand))