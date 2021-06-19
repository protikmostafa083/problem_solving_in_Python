word = input()
verify = 'hello'
j=0
for i in range(len(word)):
    if word[i]==verify[j]:
        j = j+1
    if j==5:
        break
print("YES") if j==5 else print("NO")
