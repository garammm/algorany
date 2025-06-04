# 이코테 최단 경로 실전문제 2번 미래도시 다시 풀어보기 도전
# 주의해야할 점: 노드를 기준으로 해야함
INF = int(1e9)

n,m = map(int, input().split())
# 1부터 n 까지니까 n+1
# 2차원 리스트니까 [[]*(n+1) for _ in range(n+1)]
#graph = ([INF] * (n+1) for _ in range(n+1))
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 경우 0으로 초기화
# 노드 기준이니까 m+1이 아닌 n+1
for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0


# 이어져있는 경로 값 받기.. 이게 맞나.. 그리고 각 거리의 값 1로 설정정
for _ in range(m):
    a,b = map(int, input().split())
    #graph.append((a,b))        좌표는 중요하지 않고 좌표보다 그 좌표 사이의 값이 1이라는 것이 더 중요..
    graph[a][b] = 1
    graph[b][a] = 1

x,k_node = map(int, input().split())


# 다익스트라.. 가 아니라 뭔 어쩌고 써보기
# n+1으로 써야함함
for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b]= min(graph[a][b], graph[a][k] + graph[k][b])


distance = graph[1][k_node]+graph[k_node][x]

if distance>=INF:
    print(-1)
else:
    print(distance)