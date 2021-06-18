lenword = int(input())
word = input()
count = 0
for i in range(len(word)):
    if i == len(word)-1:
        break
    if word[i]==word[i+1]:
        count = count+1
print(count)
