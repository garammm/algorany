from collections import deque
n, m = map(int,input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q_miro=deque()
q_miro.append((0,0))

while q_miro:
    x, y = q_miro.popleft()
    for i in range(4):
        nx = x+ dx[i]  
        ny = y + dy[i]

        if 0 <= nx <n and 0<=ny<m and graph[nx][ny] == 1:
            graph[nx][ny]=graph[x][y] + 1
            q_miro.append((nx,ny))


print(graph[n-1][m-1])