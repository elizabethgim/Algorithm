'''
최소 스패닝 트리 - Prim 알고리즘 이용
visited: 방문 여부를 확인
heap: 현재 그래프에서 짧은 경로를 선택


'''
import heapq
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
heap = [[0, 1]]
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])
    graph[e].append([w, s])

visited = [False] * (V+1)
answer = 0
cnt = 0
heap = [[0, 1]]
while heap:
    if cnt == V:
        break

    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        answer += w
        cnt += 1
        for i in graph[s]:
            heapq.heappush(heap, i)

print(answer)
