total_word = int(input())
lst = []
for i in range(total_word):
    word= input()
    lenword = len(word)
    if(lenword<11):
        print(word)
    else:
        print(word[0]+str(lenword-2)+word[-1])