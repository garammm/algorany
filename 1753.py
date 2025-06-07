# 하나에서 여러개 체크하니까 다익스트라로 풀어볼 예정
# 그래도 제법... 이제 푸는걸..?
import heapq

INF = int(1e9)
v,e = map(int, input().split())
k=int(input())
graph = [[] for _ in range(v+1)]
distance=[INF]*(v+1)
for _ in range(e):
    u, a, w = map(int, input().split())
    graph[u].append((a,w))         

# 꼭 while q, 그래도 이번에 거의 다 맞았네!
def dijkstra(start):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start]=0

    while q:
        cost, node = heapq.heappop(q)
        if cost>distance[node]:
            continue
        for next_node, dist in graph[node]:
            new_cost=dist+cost
            if distance[next_node]>new_cost:
                distance[next_node]=new_cost
                heapq.heappush(q,(new_cost, next_node))

dijkstra(k)

# 이 부분만 신경 쓰면 됨!
for i in range(1,v+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])


