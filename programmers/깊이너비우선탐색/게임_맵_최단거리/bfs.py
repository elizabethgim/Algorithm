from collections import deque

def solution(maps):
    answer = -1
    q = deque([(0, 0, 1)]) # x, y, v
    
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    
    while q:
        x, y, d = q.popleft()
        
        if x == n-1 and y == m-1 and visited[x][y] == True:
            answer = d
            break
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0<= ny < m:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    
                    if maps[nx][ny] == 1:
                        q.append((nx, ny, d+1))
                
                
    return answer