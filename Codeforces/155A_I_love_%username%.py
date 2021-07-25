contest = int(input())
points = list(map(int, input().split()))
cnt = 0
maxi = points[0]
mini = points[0]
for i in range(1, len(points)):
    if points[i] > points[i - 1]:
        if points[i] > maxi:
            cnt += 1
            maxi = points[i]
    elif points[i] < points[i - 1]:
        if points[i] < mini:
            cnt += 1
            mini = points[i]
    else:
        continue
print(cnt)
