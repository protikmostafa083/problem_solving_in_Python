a = int(input())
b = int(input())
c = int(input())
result = []
op1 = a+b+c
result.append(op1)

op2 = a+(b*c)
result.append(op2)

op3 = (a*b)+c
result.append(op3)

op4 = (a+b)*c
result.append(op4)

op5 = a*(b+c)
result.append(op5)

op6 = a*b*c
result.append(op6)

print(max(result))