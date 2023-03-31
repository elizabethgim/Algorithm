import sys
N = int(sys.stdin.readline())

cnt = 0

endOfWorld = [0]

i = 0

while len(endOfWorld) != N+1:
    if '666' in str(i):
        endOfWorld.append(i)
    i += 1

print(endOfWorld[N])
