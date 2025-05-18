from collections import deque

n,m = map(int,input().split())
miro_map = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

maze=deque()
maze.append((0,0))

visited=[[False]*m for i in range(n)]                 
count = 0

def bfs(y,x):
    visited[y][x] = True

    while maze:
        y,x = maze.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<m and 0<=ny<n and miro_map[ny][nx] == 1 and visited[ny][nx] == False:
                maze.append((ny,nx))
                miro_map[ny][nx] = miro_map[y][x] + 1
                visited[ny][nx] = True
                
    print(miro_map[n - 1][m - 1])


bfs(0, 0)
