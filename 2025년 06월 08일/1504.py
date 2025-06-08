import heapq

INF = int(1e9)
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))  # 양방향이니까 그래프

v1, v2 = map(int, input().split())

def dijkstra(start):
    q=[]
    distance = [INF] * (n+1)            # 왜 여기에?

    heapq.heappush(q, (0, start))
    distance[start]=0

    while q:
        dist, node = heapq.heappop(q)
        if dist>distance[node]:
            continue
        for next_node, cost in graph[node]:
            new_cost = cost + dist
            if new_cost<distance[next_node]:
                distance[next_node]=new_cost
                heapq.heappush(q,(new_cost, next_node))
    return distance                 # 있을 떄 있고 없을 때 있던데..

# 1 -> v1 -> v2 -> n 경로                
dist_from_1=dijkstra(1)
dist_from_v1=dijkstra(v1)
dist_from_v2=dijkstra(v2)

route1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]       # 이게 어떤 의미인지
route2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]

answer = min(route1, route2)

if answer >=INF:
    print(-1)
else:
    print(answer)