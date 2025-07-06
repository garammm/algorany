from collections import deque

t = int(input())
for _ in range(t):
    points = []
    n = int(input())
    for _ in range(n+2):
        x, y = map(int, input().split())
        points.append((x,y))

    graph = [[] for _ in range(n+2)]            
    
    for i in range(n+2):
        for j in range(i+1, n+2):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if abs(x2 - x1) + abs(y2 - y1) <= 1000:
                graph[i].append(j)
                graph[j].append(i)

    # bfs니까
    visited = [False]*(n+2)
    queue = deque([0])
    visited[0] = True
    
    while queue:
        point = queue.popleft()
        for next in graph[point]:
            if not visited[next]:                   # 거리가 1000보다 작은 점들 사이에 방문 안했으면 방문했다고 바꾸고 그 점을 queue에 넣는다.
                visited[next] = True
                queue.append(next)
        if point == n+1:                            # 큐에 넣은 점이 목적지에 도착하면 happy 출력
            print("happy")
            break

    else:
        print("sad")                                # 목적지에 도착 못하면 sad 출력
