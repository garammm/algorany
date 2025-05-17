from collections import deque


def solution(maps):

    n=len(maps)             # 세로 기준
    m=len(maps[0])          # 가로 기준

    visited = [[0]*m for _ in range(n)]         # 방문 횟수에 모두 0 넣기
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    short_way=deque()
    short_way.append((0,0))
    visited[0][0] = 1
    
    
    while short_way:
        x,y=short_way.popleft()
        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny] == 1 and visited[nx][ny]==0:
                    visited[nx][ny] = visited[x][y] + 1
                    short_way.append((nx,ny))
    return visited[n-1][m-1] if visited[n-1][m-1] else -1

maps = [
  [1, 0, 1, 1, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 0, 1],
  [0, 0, 0, 0, 1]
]

print(solution(maps))