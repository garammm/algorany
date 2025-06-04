# 최단 경로 전보 문제 다시 풀어보기(약간의 도움)
# 다 해보고 나니 약간의 도움이 아닌 큰 도움이었던..
# 같은 문제 내일도 해보자..

import sys
import heapq

input=sys.stdin.readline
INF = int(1e9)

n,m,c = map(int, input().split())       # n은 도시 개수 m은 통로의 개수 c는 메시지를 보내고자 하는 도시
graph = ([0] *(n+1) for _ in range(n+1))        # 그래프는 비우고고, 그리고 모든건 노드를 기준으로 이뤄진다.
distance=(INF) *(n+1)                           # 거리는 무한대로 보내놓아야 나중에 min 비교 가능능

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append[y][z]       # x에서 y 까지 z만큼 소요
    
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))         # 이젠 외워보자..
    distance[start]=0
    while q:
        dist, now = heapq.heappop(q)            # q가 익숙치 않은듯한..
        if distance[now] < dist:                # 이번엔 여기가 이해가 안되는...
            continue
        # 인접한 노드 확인인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[[i[0]]] = cost
                heapq.heappush(q, (cost,i[0]))


dijkstra(c)

count = 0
max_distance=0

for d in distance:
    if d!=INF:
        count +=1
        max_distance = max(max_distance, d)

print(count-1, max_distance)


