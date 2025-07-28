import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())            # M: 가로, N: 세로
tomato_map=[list(map(int,input().split())) for _ in range(n)]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

queue = deque()

# 시작점 해결을 위해 1인 좌표 모두 큐에 넣기
for i in range(n):
    for j in range(m):
        if tomato_map[i][j] == 1:
            queue.append((i,j))

while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<= nx < m and 0 <= ny < n and tomato_map[ny][nx]==0:
            tomato_map[ny][nx] = tomato_map[y][x]+1
            queue.append((ny, nx))

days = 0
for row in tomato_map:
    for val in row:
        if val == 0:
            print(-1)
            sys.exit(0)

    days = max(days, max(row))

print(days -1)

