# 이코테 36번 정확한 순위

n, m = map(int, input().split())
INF = int(1e9)
graph = [[]*(n+1) for _ in range(n+1)]

for i in range(m):
    graph[i][i]=0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b]=1           # 연결되어 있다는 의미로 1이라고 하면 되지

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if graph[i][j]>graph[i][k]+graph[k][j]:
                graph[i][j]=graph[i][k]+graph[k][j]   

result = 0
for i in range(1,n+1):
    count = 0
    for j in range(1,n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count+=1
    if count == n:              # N개의 배열에서 n번 비교 가능한거면 이건 위치를 알 수 있다는 것.!
        result += 1

print(result)