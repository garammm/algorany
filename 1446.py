# 생각해보면 다익스트라 조건에 맞긴 한 문제긴 해... 근데 다른게 낫지 않나라는 생각이 약간 드는데 일단 익숙한게 다익스트라니까
import heapq
INF = int(1e9)

# n은 지름길 개수, d는 고속도로의 길이
n, d = map(int, input().split())
graph=[[] for _ in range(d+1)]
distance=[INF] * (d+1)

# 다익스트라로 풀거면 기본 간선 정리먼저 들어가야함.. i에서 i+1만큼 가려면 1만큼의 거리가 필요하다
for i in range(d):
    graph[i].append((i+1,1))

for _ in range(n):
    start, end, dist= map(int, input().split())
    if end <=d:                             # 예외가 발생할 수 있으므로 이렇게 설정한다.
        graph[start].append((end, dist))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start]=0

    while q:
        cost, node = heapq.heappop(q)
        if distance[node]<cost:
            continue
        for next_node, dist in graph[node]:
            new_cost = cost + dist
            if new_cost < distance[next_node]:
                distance[next_node]=new_cost
                heapq.heappush(q, (new_cost, next_node))

dijkstra(0)                 # 시작점이 0이니까
print(distance[d])

