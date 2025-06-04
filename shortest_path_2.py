# 이코테 최단경로 실전문제 2번
# 우선 적어보며 이해하고 암기해보자

INF = int(1e9)

n,m = map(int, input().split())
# 2차원 리스트를 만들고, 모든 값을 무한으로
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

# 입력받기
for _ in range(m):
    # A와 B가 서로에게 가는 비용은 1이라고 설정
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

# 거쳐 갈 노드 x와 최종 목적지 노드 K를 입력받기
x, k =map(int,input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
# 중간 지점점
for k in range(1,n+1):
    # 시작 지점점
    for a in range(1,n+1):
        # 종료 시점점
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= INF:
    print("-1")
# 도달할 수 있다면, 최단 거리를 출력
else:
    print(distance)