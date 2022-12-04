import sys
hour, mininute = map(int, sys.stdin.readline().split(' '))
cook = int(sys.stdin.readline())

mininute += cook
if mininute > 59:
    hour += mininute // 60
    mininute = mininute % 60

if hour >= 24:
    hour = hour % 24
print(hour, mininute)