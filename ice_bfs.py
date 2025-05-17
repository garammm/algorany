from collections import deque

n, m = map(int, input().split())
icer = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    icer[x][y] = 1  # 방문 처리

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and icer[nx][ny] == 0:
                icer[nx][ny] = 1
                queue.append((nx, ny))
    
    return True

result = 0
for i in range(n):
    for j in range(m):
        if icer[i][j] == 0:
            if bfs(i, j) == True:
                result += 1

print(result)
