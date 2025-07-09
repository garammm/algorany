# dfs 공부의 목적으로 책에 있는 코드 적으며...
n,m = map(int, input().split())                 # 세로 n, 가로 m

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    # 범위 벗어나면 즉시 종료
    if x <= -1 or x >= n or y<=-1 or y>=m:                  # x는 n, 즉 세로랑 비교
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y]==1
        # 상하좌우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1

print(result)