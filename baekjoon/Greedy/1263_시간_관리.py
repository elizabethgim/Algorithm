N = int(input())
work = []
# t: 걸리는 시간, s: 끝나는 시간
for _ in range(N):
    t, s = map(int, input().split())
    work.append((s, t))

work.sort(reverse=True)

start = work[0][0]-work[0][1]
prev = 0
for i in range(N):
    ss = work[i][0]
    tt = work[i][1]

    if prev != ss:
        if ss-tt < start:
            start = ss-tt
    else:
        start -= tt
    prev = ss

if start < 0:
    start = -1

print(start)

'''
3
1 10
3 10
5 10
'''