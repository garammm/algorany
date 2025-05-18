from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        visited[y][x] = 1

        while queue:
            cx, cy = queue.popleft()
            for i in range(4):
                nx = cx+dx[i]
                ny = cy+dy[i]
                if 0 <= nx <m and 0 <=ny < n:
                    if baechu[ny][nx] == 1 and visited[ny][nx] == 0:
                        queue.append((nx,ny))
                        visited[ny][nx] = 1


T = int(input())

for _ in range(T):
    m,n,k = map(int,input().split())
    baechu = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]

    for _ in range(k):
        x,y = map(int,input().split())
        baechu[y][x] = 1

    count = 0
    for y in range(n):
        for x in range(m):
            if baechu[y][x] == 1 and visited[y][x] == 0:
                bfs(x,y)
                count += 1
    print(count)
