from collections import deque

n, m = map(int, input().split())        
treasure_map = [list(input()) for _ in range(n)]

def bfs(x,y):
    visited = [[-1]*m for _ in range(n)]
    visited[x][y]=0
    q=deque()
    q.append((x,y))
    max_dist = 0

    while q:
        cx, cy = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < n and 0 <= ny <m:
                if treasure_map[nx][ny] == 'L' and visited[nx][ny] == -1:
                    visited[nx][ny]=visited[cx][cy] + 1
                    max_dist = max(max_dist, visited[nx][ny])
                    q.append((nx,ny))

    return max_dist

result = 0
for i in range(n):
    for j in range(m):
        if treasure_map[i][j]=='L':
            result = max(result, bfs(i,j))

print(result)    
