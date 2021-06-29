def swap_case(s):
    word = []
    for i in range(len(s)):
        if ord(s[i]) >=65 and ord(s[i])<=90:
            word.append(s[i].lower())
        elif ord(s[i]) >=97 and ord(s[i])<=122:
            word.append(s[i].upper())
        else:
            word.append(s[i])
    return "".join(word)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
