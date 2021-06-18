uname = input()
used = []
for i in range(len(uname)):
    if uname[i] not in used:
        used.append(uname[i])
if len(used)%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')