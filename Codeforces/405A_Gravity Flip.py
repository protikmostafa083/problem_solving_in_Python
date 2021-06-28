col = int(input())
balls = list(map(int, input().split()))
balls.sort()
print(*balls, sep=' ')