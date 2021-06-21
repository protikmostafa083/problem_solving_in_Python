year = int(input())
i = year + 1
while i < 100000:
    lenst = len(set(list(str(i))))
    if lenst<4:
        i=i+1
    else:
        break
print(i)
