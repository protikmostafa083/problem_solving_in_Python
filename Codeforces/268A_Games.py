testCase = int(input())
g1 = []
g2 = []
for i in range(testCase):
    n1, n2 = map(int, input().split())
    g1.append(n1)
    g2.append(n2)
cnt = 0
for j in range(len(g1)):
    if g1[j] in g2:
        cnt += g2.count(g1[j])
print(cnt)
