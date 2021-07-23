total = list(input()) + list(input())
total.sort()
found = list(input())
found.sort()
if total == found:
    print('YES')
else:
    print('NO')
