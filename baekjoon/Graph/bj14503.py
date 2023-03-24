dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
place = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

visited[r][c] = 1
cnt = 1

while True:
    back = True
    for _ in range(4):
        d = (d+3) % 4
        nr = r + directions[d][0]
        nc = c + directions[d][1]

        if 0 <= nr < N and 0 <= nc < M and place[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                cnt += 1
                r = nr
                c = nc
                back = False
                break
    if back:
        if place[r-directions[d][0]][c-directions[d][1]] == 1:
            print(cnt)
            break
        else:
            r, c = r-directions[d][0], c-directions[d][1]

print(*place, sep="\n")

'''
[1,  1,  1,  1,  1,  1,  1,  1,  1, 1]
[1, 56, 57, 46, 45, 44, 43, 42, 41, 1]
[1, 55, 48, 47,  1,  1,  1,  1, 40, 1]
[1, 50, 49,  1,  1, 36, 37, 38, 39, 1]
[1, 51,  1,  1, 35, 34, 31, 30,  0, 1]
[1, 52, 53, 12, 11, 33, 32, 29, 28, 1]
[1, 54, 14, 13, 10,  9,  0,  1, 27, 1]
[1, 16, 15,  2,  0,  8,  1,  1, 26, 1]
[1, 17, 18,  3,  4,  7,  1,  1, 25, 1]
[1, 21, 19, 20,  5,  6, 22, 23, 24, 1]
[1,  1,  1,  1,  1,  1,  1,  1,  1, 1]


[1,  1, 1, 1, 1, 1, 1, 1, 1, 1]
[1,  0, 0, 0, 0, 0, 0, 0, 0, 1]
[1,  0, 0, 0, 1, 1, 1, 1, 0, 1]
[1,  0, 0, 1, 1, 0, 0, 0, 0, 1]
[1,  0, 1, 1, 0, 0, 0, 0, 0, 1]
[1,  0, 0, 12, 11, 0, 0, 0, 0, 1]
[1,  0, 14, 13, 10, 9, 0, 1, 0, 1]
[1, 16, 15, 2, 0, 8, 1, 1, 0, 1]
[1, 17, 18, 3, 4, 7, 1, 1, 0, 1]
[1, 21, 19, 20, 5, 6, 0, 0, 0, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

Process finished with exit code 0

'''
