from collections import deque

n,m = map(int,input().split())
gallery = [list(map(int,input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 방문 여부 체크용 (생각하지 못했던 부분)
visited = [[False]*m for _ in range(n)]


picture_count = 0
max_area = 0

def bfs(x,y):
    paint = deque()
    paint.append((x, y))
    visited[x][y] = True
    area = 1                # 현재 그림의 넓이이

    while paint:
        cx,cy = paint.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and gallery[nx][ny] ==1:
                    paint.append((nx,ny))
                    visited[nx][ny]=True
                    area += 1
    return area

for i in range(n):
    for j in range(m):
        if gallery[i][j] == 1 and not visited[i][j]:
            picture_count += 1
            max_area=max(max_area, bfs(i,j))

print(picture_count)
print(max_area)