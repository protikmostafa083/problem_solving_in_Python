word=input().lower()
for i in range(len(word)):
    if(word[i]=='a' or word[i]=='o' or word[i]=='y' or word[i]=='e' or word[i]=='u' or word[i]=='i'):
        continue
    else:
        print('.'+word[i],end='')