num = int(input())
gameOutcome = list(input())
anton = gameOutcome.count('A')
danik = gameOutcome.count('D')
if anton>danik:
    print('Anton')
elif danik>anton:
    print('Danik')
else:
    print('Friendship')