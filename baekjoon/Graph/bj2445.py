import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0 for _ in range(N+1)]
cnt = 1
def bfs(start):
    global cnt
    que = deque()
    que.append(start)
    visited[start] = 1

    while que:
        u = que.popleft()
        graph[u].sort(reverse=True)
        for v in graph[u]:
            if not visited[v]:
                cnt += 1
                visited[v] = cnt
                que.append(v)

bfs(R)

for i in range(1, N+1):
    print(visited[i])