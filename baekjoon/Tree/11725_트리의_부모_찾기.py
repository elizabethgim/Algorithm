from cgitb import reset
from collections import deque

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0 for _ in range(N+1)]

queue = deque()
queue.append(1)

def bfs():
    while queue:
        next = queue.popleft()
        for now in graph[next]:
            if parent[next] == 0:
                parent[next] = now
                queue.append(next)

bfs()

result = parent[2:]
print(*result, sep="\n")
