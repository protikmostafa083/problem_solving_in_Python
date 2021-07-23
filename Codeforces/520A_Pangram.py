standard = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphCount = int(input())
word = input()
if alphCount<26:
    print('NO')
else:
    word = word.lower()
    word = set(word)
    word = sorted(word)
    if word == standard:
        print('YES')
    else:
        print('NO')