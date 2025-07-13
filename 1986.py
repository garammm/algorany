import sys
input = sys.stdin.readline

# q,k,p 입력값 받기
n, m = map(int, input().split())        # m개씩 n줄


total_map =[[0]*m for _ in range(n)]

# queen
raw = list(map(int, input().split()))
q = raw[0]
q_map = []
if q > 0:
    for i in range(q):
        x, y = raw[1 + i * 2], raw[2 + i * 2]
        x -= 1
        y -= 1
        q_map.append((x, y))
        total_map[x][y] = 1

# knight
raw = list(map(int, input().split()))
k = raw[0]
k_map = []
if k > 0:
    for i in range(k):
        x, y = raw[1 + i * 2], raw[2 + i * 2]
        x -= 1
        y -= 1
        k_map.append((x, y))
        total_map[x][y] = 1

# pawn
raw = list(map(int, input().split()))
p = raw[0]
p_map = []
if p > 0:
    for i in range(p):
        x, y = raw[1 + i * 2], raw[2 + i * 2]
        x -= 1
        y -= 1
        p_map.append((x, y))
        total_map[x][y] = 1


# queen의 공격
queen_dirs=[(-1,0), (1,0), (0,-1), (0, 1), (-1, -1), (-1,1), (1, -1), (1,1)]

for x, y in q_map:
    for dx, dy in queen_dirs:
        nx, ny =x+dx, y+dy
        while 0 <=nx < n and 0 <=ny <m:
            #다른 말이 있으면 공격 끝
            if total_map[nx][ny]==1:
                break
            # 아직 공격 안한 칸
            if total_map[nx][ny]==0:
                total_map[nx][ny]=2
            # 다음칸으로 이동
            nx += dx
            ny += dy

# knight의 공격
knight_dirs=[(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1, 2), (2,-1),(2,1)]

# knight는 한번만 가면 되니까
for x, y in k_map:
    for dx, dy in knight_dirs:
        nx, ny =x+dx, y+dy
        if 0<=nx<n and 0<=ny<m:
            # 아직 공격 안한 칸
            if total_map[nx][ny]==0:
                total_map[nx][ny]=2
          

count = 0
for i in range(n):
    for j in range(m):
        if total_map[i][j]==0:
            count+=1

print(count)