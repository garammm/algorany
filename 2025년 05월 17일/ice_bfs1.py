from collections import deque

n ,m = map(int,input().split())
ice_maker = [list(map(int, input().strip())) for _ in range(n)]


dx =[-1, 1, 0, 0]
dy = [0,0, -1, 1]

visited =[[False] * m for _ in range(n)]


count = 0 

def bfs(y, x):
    icream = deque()
    icream.append((y,x))
    visited[y][x] = True
    
    while icream:
        y, x = icream.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and ice_maker[ny][nx]==0 and visited[ny][nx]==False:
                icream.append((ny, nx))
                visited[ny][nx]=True

for a in range(n):
    for b in range(m):
        if visited[a][b] == False and ice_maker[a][b] == 0:
            bfs(a,b)
            count +=1

print(count)
     
