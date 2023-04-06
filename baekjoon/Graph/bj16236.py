from collections import deque

N = int(input())
sea = []
for _ in range(N):
    sea.append(list(map(int, input().split())))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs(start_x, start_y, sharkSize):
    fishes = []
    que = deque()
    visited = [[False]*N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]

    que.append((start_x, start_y))
    visited[start_x][start_y] = True

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고,
                if sea[nx][ny] <= sharkSize:
                    que.append((nx, ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    if sea[nx][ny] < babyshark and sea[nx][ny] != 0:
                        fishes.append((distance[nx][ny], nx, ny))

    fishes.sort()

    return fishes

time = 0
babyshark = 2
eaten = 0
while True:
    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:
                x = i
                y = j
                sea[i][j] = 0

    start = (x, y)

    canEat = bfs(x, y, babyshark)

    if len(canEat) == 0:
        break

    dd, xx, yy = canEat[0]
    time += dd
    eaten += 1
    sea[xx][yy] = 9

    if babyshark == eaten:
        babyshark += 1
        eaten = 0

print(time)
