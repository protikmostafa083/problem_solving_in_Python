m,n = map(int, input().split())
if(m*n %2 == 0):
    print(m*n//2)
else:
    print(int((m*n)-1)//2)