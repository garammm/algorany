# 백준 18352 문제
# 다익스트라로 생각했는데 bfs로 풀 수 있대서 이 풀이도 첨부
# 좀이따 안보고 풀어보자
'''
import heapq

n,m,k = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1)) 

def dijkstra(start):
    q =[]
    heapq.heappush(q, (0,start))        # (거리, 노드)
    distance[start] = 0                 # 이것이 기본 다익스트라 구조

    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for next_node, cost in graph[now]:
            new_cost=dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))

dijkstra(k)

found = False
for i in range(1, n+1):
    if distance[i] ==k:
        print(i)
        found = True

if not found:
    print(-1)
'''

from collections import deque

# n: 도시 개수, m: 도로 개수, k: 목표 거리, start: 시작 도시
n,m,k,start = map(int,input().split())

graph = [[] for _ in range(n+1)]        # 1~n
distance = [-1] * (n+1)                 # -1을 방문하지 않은 걸로 잡고 푼다

# 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)                  # 단방향 그래프

# BFS를 위한 큐 초기화
queue = deque([start])
distance[start] = 0

while queue:
    now=queue.popleft()
    for next_node in graph[now]:
        if distance[next_node]==-1:
            distance[next_node] = distance[now] +1

found = False
for i in range(1, n+1):
    if distance[i] ==k:
        print(i)
        found = True

if not found:
    print(-1)





