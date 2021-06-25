rot = int(input())
prev_inp = input()
count = 1
for i in range(rot-1):
    new_inp = input()
    if new_inp != prev_inp:
        count += 1
        prev_inp = new_inp
print(count)
