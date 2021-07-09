lantern, distance = map(int, input().split())
lanDis = list(map(int, input().split()))
lanDis.sort()
dis1 = lanDis[0]-0
dis3 = distance - lanDis[-1]
dis2 = 0
for i in range(len(lanDis) - 1):
    newDis = lanDis[i + 1] - lanDis[i]
    if newDis > dis2:
        dis2 = newDis
dis2 = dis2 / 2

print(float(max(dis1, dis2, dis3)))