myLan = ['H', 'Q', '9']
word = list(input())
flag = 0
for i in range(len(word)):
    if word[i] in myLan:
        flag = 1
        break
    else:
        flag = 0
print('YES') if flag==1 else print('NO')
