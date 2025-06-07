# 다익스트라로 풀거야. 다시 풀어보기 도전
import heapq

INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance=[INF] * (n+1)              # 거리 이거 어디서부터 어디까지 거리로 잡는거였지? 시작점 거리?

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1))          # a부터 b까지 거리 1

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))            # 거리, 노드 순으로 넣어야  heapq 사용 가능
    distance[start]=0
    while q:
        dist, node = heapq.heappop()
        if distance[node] < dist:
            continue
        for next_node, cost in graph[node]:
            new_cost = dist+cost
            if new_cost<distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))


dijkstra(x)

found = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        found = True

if not found:
    print(-1)
