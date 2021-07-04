inSet = set(input())
count = 0
for i, val in enumerate(inSet):
    if (65 <= ord(val) <= 90) or (97 <= ord(val) <= 122):
        count += 1
print(count)
