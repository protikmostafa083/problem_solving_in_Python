word = input()
count = 0
for i in range(len(word)):
    if word[i] == '4' or word[i] == '7':
        count += 1
if count == 4 or count == 7:
    print('YES')
else:
    print('NO')
