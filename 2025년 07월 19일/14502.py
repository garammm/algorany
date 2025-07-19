# 다음에 꼭 풀어보기
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
lab_map = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 빈칸 위치 모으기
empty=[]
for i in range(n):
    for j in range(m):
        if lab_map[i][j] == 0:
            empty.append((i, j))


def bfs(temp_map):
    q=deque()

    # 바이러스 위치 큐에 추가
    for i in range(n):
        for j in range(m):
            if temp_map[i][j]==2:
                q.append((i,j))

    while q:
        y, x = q.popleft()       
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<m and 0<=ny<n:
                if temp_map[ny][nx] == 0:
                    temp_map[ny][nx] = 2
                    q.append((ny, nx))

max_safe=0

# 이 부분 진짜 외우기 걍 외워... 어렵다아아아아
for walls in combinations(empty, 3):
    # 맵 복사
    temp_map = [row[:] for row in lab_map]

    # 벽 세우기
    for x, y in walls:
        temp_map[x][y]=1

    # 바이러스 퍼뜨리기
    bfs(temp_map)

    safe = sum(row.count(0) for row in temp_map)
    max_safe = max(max_safe, safe)

print(max_safe)