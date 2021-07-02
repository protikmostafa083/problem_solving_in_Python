candle, reconTH = map(int, input().split())
hour = candle
remaining = 0
while candle >= reconTH:
    remaining = candle % reconTH
    candle = (candle - remaining) / reconTH
    hour = hour + candle
    candle = candle + remaining
print(int(hour))