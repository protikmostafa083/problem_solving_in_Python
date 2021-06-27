n = int(input())
for i in range(1, n+1):
    if i==1:
        print('I hate', end = ' ')
    if i>=3 and i%2==1:
        print('that I hate', end = ' ')
    if i>=2 and i%2==0:
        print('that I love', end = ' ')
print('it')