from collections import deque

n = int(input())
apartment = [list(map(int, input().strip())) for _ in range(n)]
queue = deque()
visited =[[0]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()                     # 안에서 큐 만들어야 혀....
    queue.append((x,y))                 # 피티야 왜 여기 0,0 안넣어..? -> 이거 시작점이 없자너. 그래서 0,0 넣으면 안된대
    visited[y][x] = 1
    count = 1                           # 시작점 넓이 1 포함해주는 것
    while queue:
        #queue.append((0,0))            # 0 안넣어도 된다...
        x,y = queue.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < n and 0 <=cy<n and apartment[cy][cx]==1 and visited[cy][cx]==0:
                visited[cy][cx] +=1                             # 방문 했고
                queue.append((cx,cy))                           # 큐에 넣고
                #apartment[cy][cx]=apartment[x][y] + 1           # 이건 최단거리 구할 때 하는거구... 지금은 크기 구하고 있자너?
                count +=1
    return count                                    # 항상 어디에 리턴해야하나 고민하는데 while문에 맞춰야지 큐 비었을 때 가능혀
        
areas = []                                   # 넓이 구한거 넣으려고 만들어 놓다

for b in range(n):
    for a in range(n):
        if apartment[b][a] == 1 and visited[b][a] == 0:
            area = bfs(a,b)                         # 아놔 x,y 헷갈리네... 적을때마다 생각하자... 여긴 배열이다..
            areas.append(area)

areas.sort()                                        # 이것은 올림차순 정렬, 그리디 할 떄 햇엇음 이 부분 피티가 함.. 나중에꼬옥다시해보기
print(len(areas))                                   # 개수 먼저 출력
for a in areas:
    print(a)                                        # 리스트에 있는거 출력!
