N, H, W = map(int, input().split())

words = []
for i in range(H):
    words.append(list(j for j in input().strip()))

visited = [[False for _ in range(N*W)] for _ in range(H)]

answer = ""

for i in range(H):
    for j in range(N*W):
        if not visited[i][j]:
            visited[i][j] = True
            tmp = words[i][j]

            for ii in range(H):
                for jj in range(W):
                    n = i+ii
                    m = j+jj
                    visited[n][m] = True
                    if tmp == '?' and tmp != words[n][m]:
                        tmp = words[n][m]

            answer += tmp

print(answer)
