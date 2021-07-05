n, m = map(int, input().split())
days = n
days = days + int(days//m)
if (days%m==0):
    print(days+1)
else:
    print(days)