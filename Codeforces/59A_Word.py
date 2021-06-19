word = input()
count = 0
#print(ord(a))
for i in range(len(word)):
    if ord(word[i])<97:
        count = count+1
if(count>(len(word)/2)):
    print(word.upper())
else:
    print(word.lower())