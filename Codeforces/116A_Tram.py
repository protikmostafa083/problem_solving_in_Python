rotation = int(input())
passenger, capacity = 0, 0
for i in range(rotation):
    salida, entrada = map(int, input().split())
    passenger = passenger+entrada-salida
    if passenger>capacity:
        capacity = passenger
print(capacity)