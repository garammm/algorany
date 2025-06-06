# 최단 경로 실전 문제 3번 전보
# 3번쨰

# 이걸 까먹다니..
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9) 


# n은 도시 개수, m은 통로 개수, c는 메시지를 보내고자 하는 도시
n, m, c = map(int, input().split())

# 그래프는 비어놓기
graph = [[] for _ in range(n+1)]

# 거리 테이블은 무한으로 초기화
distance = [INF] * (n+1)

# 정보 입력받기
for _ in range(m):
    x, y, z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입한대
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:                        # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(c)

# 개수 새려고 
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    # 도달할 수 있는 노드
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드 -1
print(count-1, max_distance)


