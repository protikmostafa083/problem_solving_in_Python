limak, bob = map(int, input().split())
count = 0
while True:
    if limak>bob:
        break
    else:
        limak = limak*3
        bob = bob*2
        count = count +1
print(count)