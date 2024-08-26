from collections import deque

N, H, W = map(int, input().split())

words = []
for i in range(H):
    words.append(list(j for j in input().strip()))

words2 = [['' for _ in range(N*W)] for _ in range(H)]
visited = [[False for _ in range(N*W)] for _ in range(H)]

answer = ""

for i in range(H):
    for j in range(N*W):
        if not visited[i][j]:
            visited[i][j] = True
            words2[i][j] = words[i][j]
            answer += words[i][j]

            for ii in range(H):
                for jj in range(W):
                    n = i+ii
                    m = j+jj
                    words2[n][m] = words[i][j]
                    visited[n][m] = True

print(answer)


def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        
        for i in range(H):
            for j in range(W):
                visited[i][j] = True