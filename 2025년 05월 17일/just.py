from collections import deque


n,m = map(int,input().split()) 
miro = [list(map(int, input().strip())) for _ in range(n)] # split이 아니라 \n 없애는 거였는데 아 제발 이제는 기억하자 strip 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
way = deque()
way.append((0, 0))

while way:
    x, y = way.popleft()
    for i in range(4):
        nx = x+ dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and miro[nx][ny] == 1:
            miro[nx][ny] = miro[x][y] +1
            way.append((nx, ny))


print(miro[n-1][m-1])
