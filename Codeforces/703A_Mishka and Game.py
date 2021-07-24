rounds = int(input())
battery = 0
for i in range(rounds):
    m,c = map(int, input().split())
    if m>c:
        battery += 1
    elif m<c:
        battery -= 1
    else:
        continue
if battery>0:
    print('Mishka')
elif battery<0:
    print('Chris')
else:
    print('Friendship is magic!^^')