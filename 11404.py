# 백준 11404 플로이드
# 다익스트라 하느라 플로이드 오랜만이어서 지금 한번 보면서 이해해봤는데 좀이따 꼭 다시 해보자
n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0
for i in range(1, n+1):
    graph[i][i] = 0

# 플로이드는 graph[a][b]=c 이런식으로 데이터 받아야함
for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b]>c:
        graph[a][b]=c

# 플로이드-와샬 알고리즘
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# 결과 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end = ' ')

    print()         # 줄 바꿈용


