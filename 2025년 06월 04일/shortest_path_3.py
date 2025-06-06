# 이코테 최단 경로 실전문제 3번 전보
# 우선 따라 적어보며 익혀보자

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)  

# 노드드의 개수, 간선의 개수, 시작 노드를 입력받기
n, m, start =map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF]*(n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    w,y,z = map(int, input().split())
    # x번 노드에서 y 번 노드로 가는 비용이 z란 의미
    graph[w].append((y,z))

def dijkstra(start):
    q=[]
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q,(0,start))         # 이부분 이해 x
    distance[start] = 0
    while q:    # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]          # cost가 어디서 뭐하려고 튀어나온지를 모르겠네 -> 현재 거리 + 다음 노드까지의 거리리
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance=max(max_distance ,d)

# 시작 노드는 제외해야 하므로 count-1 dmf cnffur
print(count-1, max_distance)
