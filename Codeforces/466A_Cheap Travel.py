# defining variables
nTravel, mRIdes, aCostPerTicket, bCostofMRIdes = map(int, input().split())
# logic implementation
# using only the one ticket cost
price1 = nTravel * aCostPerTicket
# using special and basic costs focusing on special ticket
price2 = int(nTravel // mRIdes) * bCostofMRIdes + int(nTravel % mRIdes) * aCostPerTicket
# using special and basic costs focusing on special ticket
price3 = (nTravel + 1) * aCostPerTicket
# using only the special amount
if nTravel % mRIdes == 0:
    price4 = (nTravel / mRIdes) * bCostofMRIdes
else:
    price4 = (int(nTravel // mRIdes) + 1) * bCostofMRIdes

print(min(price1, price2, price3, price4))
