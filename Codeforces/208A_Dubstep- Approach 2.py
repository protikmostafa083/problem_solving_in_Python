word = input()
word = word.split('WUB')
new = []
for i in range(len(word)):
    if word[i] == '':
        continue
    else:
        new.append(word[i])
print(" ".join(new))
