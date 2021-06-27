word = input()
flag, count = 0, 0
for i in range(0, len(word)):
    if ord(word[i]) < 97:
        flag = 1
        count += 1
    else:
        flag = 0
        if i == 0:
            continue
        else:
            break

if flag == 1 and count == len(word) - 1:
    print(word[0].upper() + word[1:].lower())
elif flag == 0 and len(word) == 1:
    print(word.upper())
elif flag == 1 and count == len(word):
    print(word.lower())
else:
    print(word)
