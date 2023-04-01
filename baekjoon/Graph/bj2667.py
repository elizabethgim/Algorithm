import sys
from collections import deque

N = int(sys.stdin.readline())
graph = []

for _ in range(N):
    graph.append(list(int(x) for x in sys.stdin.readline().strip()))


def bfs(start, cnt):
    que = deque()
    que.append(start)
    graph[start[0]][start[1]] = cnt
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    house = 1

    while que:
        x, y = que.popleft()

        for n in range(4):
            xx = x + dx[n]
            yy = y + dy[n]
            if 0 <= xx < N and 0 <= yy < N and graph[xx][yy] == 1:
                que.append((xx, yy))
                graph[xx][yy] = cnt
                house += 1

    return house


cnt = 1
houses = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt += 1
            total = bfs((i, j), cnt)
            houses.append(total)


houses.sort()
print(cnt - 1)
print(*houses, sep='\n')

'''
5
00001
00000
10000
00000
00000
'''