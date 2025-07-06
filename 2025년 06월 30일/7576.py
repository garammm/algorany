from collections import deque

m, n = map(int, input().split())        # m 가로 n 세로
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

# 익은 토마토 위치 큐에 넣기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))

# 복습!
def bfs():
    while queue:
        x,y = queue.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            # 범위 체크 새로x 가로y
            if 0 <= nx < n and 0 <= ny < m:
                # 익지 않은 토마토면 익히기
                if graph[nx][ny]


for i in range(m):
    for j in range(n):
        if dfs(i,j)==True:
            

print(result)