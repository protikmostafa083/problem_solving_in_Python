init_price, money_has, banana_want = map(int, input().split())
needed_money = 0
for i in range(1,banana_want+1):
    needed_money = needed_money + (i*init_price)
if needed_money<money_has:
    print('0')
else:
    print(needed_money-money_has)