import sys
from collections import deque

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

T = int(sys.stdin.readline())
def bfs(start, end):
    que = deque()
    que.append(start)
    cnt = 0
    visited[start[0]][start[1]] = True

    while que:
        night = que.popleft()
        x = night[0]
        y = night[1]

        for i in range(8):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < l and 0 <= yy < l and not visited[xx][yy]:
                arr[xx][yy] = arr[x][y] + 1
                visited[xx][yy] = True
                que.append((xx, yy))

    return arr

for _ in range(T):
    l = int(sys.stdin.readline())
    curr = list(map(int, sys.stdin.readline().split()))
    to = list(map(int, sys.stdin.readline().split()))

    arr = [[0]*l for _ in range(l)]
    visited = [[False]*l for _ in range(l)]

    answer = bfs(curr, to)
    print(answer[to[0]][to[1]])


'''
8
0 0
7 0
'''