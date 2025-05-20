# 구하려는 것: 색칠 안 된 영역 개수, 영역 크기기
# DFS 알고리즘 스터디 문제
m, n, k = map(int, input().split())  # 세로, 가로, 사각형 개수

# 그래프 초기화: m행 n열 (세로 x 가로)
graph = [[0] * n for _ in range(m)]
visited = [[0] * n for _ in range(m)]
result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 사각형 정보 입력 받기
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):         # 세로 (행)
        for j in range(x1, x2):     # 가로 (열)
            graph[i][j] = 1         # 사각형 칠해진 부분

# 넓이 구하기 위한 dfs
def dfs(x, y):
    global area                     # 함수 안에서 값을 변경하기 위해해
    visited[x][y] = True
    area += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] == 0:
                dfs(nx, ny)

# dfs 함수 이용해서 정리
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and visited[i][j] == 0:
            area = 0
            dfs(i,j)
            result.append(area)

result.sort()
print(len(result))
print(*result)                       # 원소 나란히 출력

