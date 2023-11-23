N = int(input())
work = []
# t: 걸리는 시간, s: 끝나는 시간
for _ in range(N):
    t, s = map(int, input().split())
    work.append((s, t))

work.sort(reverse=True)

start = work[0][0]-work[0][1]   # 가장 늦게 일어날 수 있는 시간
prev = 0

for i in range(N):
    ss = work[i][0]
    tt = work[i][1]

    # 끝나는 시간이 start보다 작으면
    if ss < start:
        start = ss-tt
    else:
        start -= tt

if start < 0:
    start = -1

print(start)

'''
3
1 10
3 10
5 10
'''