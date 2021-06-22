command = int(input())
lst = []
for i in range(command):
    inp = input().split()
    if inp[0] == 'insert':
        lst.insert(int(inp[1]), int(inp[2]))
    if inp[0] == 'print':
        print(lst)
    if inp[0] =='remove':
        lst.remove(int(inp[1]))
    if inp[0] == 'append':
        lst.append(int(inp[1]))
    if inp[0] == 'sort':
        lst.sort()
    if inp[0]=='pop':
        lst.pop()
    if inp[0]=='reverse':
        lst.reverse()
