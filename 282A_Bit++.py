rotation = int(input())
count = 0
for i in range(rotation):
    raw = input()
    if(raw == '++X' or raw == 'X++'):
        count = count+1
    else:
        count = count-1
print(count)