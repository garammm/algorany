# 아진짜 뿌듯. 해내다
import heapq

INF = int(1e9)
# 도시 개수
n=int(input())
# 버스 개수
m=int(input())
# 버스 정보 넣을 그래프
graph = [[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end,cost))

start_city, destination = map(int, input().split())
    
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0, start))
    distance[start]=0

    while q:
        dist, end_node = heapq.heappop(q)           # 순서 주의
        if distance[end_node]< dist:
            continue
        for next_node, money in graph[end_node]:
            new_cost = money + dist
            if distance[next_node]>new_cost:
                distance[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))

dijkstra(start_city)
if distance[destination] <INF:
    print(distance[destination])