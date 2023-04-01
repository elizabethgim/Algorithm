import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

bfs_visited = [False for _ in range(N+1)]
def bfs(start, cnt):
    que = deque([start])
    bfs_visited[start] = True
    print(start, end=' ')

    while que:
        x = que.popleft()
        graph[x].sort()
        for i in graph[x]:
            if not bfs_visited[i]:
                bfs_visited[i] = True
                print(i, end=' ')
                que.append(i)

dfs_visited = [False for _ in range(N+1)]
def dfs(x, cnt):
    print(x, end=' ')
    dfs_visited[x] = True
    graph[x].sort()

    for i in graph[x]:
        if not dfs_visited[i]:
            dfs(i, cnt)


dfs(V, 0)
print()
bfs(V, 0)
