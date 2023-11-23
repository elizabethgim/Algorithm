import copy

board = [[[] for _ in range(4)] for _ in range(4)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    arr = list(map(int, input().split()))
    for j in range(8):
        if j % 2 == 0:
            board[i][j//2].append(arr[j])
        else:
            board[i][j//2].append(arr[j])

print(*board, sep='\n')

max_score = 0


def dfs(x, y, score, sea):
    global max_score
    score += sea[x][y][1]
    sea[x][y][0] = 0

    for f in range(1, 17):
        for i in range(4):
            for j in range(4):
                if sea[i][j][0] == f:
                    d = sea[i][j][1]
                    break

        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
            continue

        sea[nx][ny], sea[x][y] = sea[x][y], sea[nx][ny]

