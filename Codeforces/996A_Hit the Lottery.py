money = int(input())
answer = money // 100
left = money % 100

answer += left // 20
left = left % 20

answer += left // 10
left = left % 10

answer += left // 5
left = left % 5

answer += left

print(answer)
