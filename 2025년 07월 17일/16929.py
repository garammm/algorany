import sys

# 나중에 다시 풀어보자...
# 진짜 복잡한 dfs 였어...
n, m = map(int, input().split())
dot_list = [list(input().strip()) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def dfs(x, y, from_x, from_y, color):
    visited[x][y] = 1           # 시작하는 지점 visited=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if (nx, ny) == (from_x, from_y):
                continue
            if dot_list[nx][ny] == color:
                if visited[nx][ny] == 1:
                    return True
                else:
                    if dfs(nx, ny, x, y, color) == 1:
                        return True
    return False

for i in range(n):
    for j in range(m):
        if visited[i][j]==0:           
            if dfs(i, j, -1, -1, dot_list[i][j]) == True:
                print("Yes")
                sys.exit(0)
print("No")