# 최단 경로 실전 문제 미래도시 문제 3번쨰 복습..
# 오랜만에 풀려니 다시 거의 보고 적는 느낌으로 푸는..
# 그럼에도 해야지

# 이런 문제 풀 때는 무조건 무한대 하나 설정
INF = int(1e9)

# n이 노드, m이 간선의 개수
n, m = map(int, input().split())
# 노드 사이 거리값 넣을 그래프에 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는건 0으로 해놓기
for a in range(1,n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B까지 거리 1,
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 점화식에 따라 플로이드 위셜 알고리즘 이용!
for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph [k][b]

if distance >= INF:
    print("-1")
else:
    print(distance)


