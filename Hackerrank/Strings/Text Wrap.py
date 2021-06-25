word = input()
rot = int(input())
    for i in range(0, len(word), rot):
        print(word[i: i+rot])