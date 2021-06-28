thlevel = int(input()) #level to pass the game
#taking the number of games and game level that x passed
xgame, *xlevel = input().split()
xlevel = list(map(int, xlevel))
#taking the number of games and game level that x passed
ygame, *ylevel = input().split()
ylevel = list(map(int, ylevel))
#merging xlevel and ylevel
help = xlevel + ylevel
#removing duplicated
help = list(dict.fromkeys(help))
#condition and voila!
if len(help)==thlevel:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
