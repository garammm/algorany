# 최단 거리 문제는 bfs로..!
# 1번째
from collections import deque
n, m, k, x = map(int,input().split())
city = [[] for _ in range(n+1)]     # 왜 n이 아니라 n+1? => 왜냐면 도시번호가 1~4고 0번을 비워놓았기 때문
for _ in range(m):
    a,b = map(int, input().split())
    city[a].append(b)               # 튜플이 아닌 이 방법으로 a,b 할당당

distance = [-1]*(n+1)               # 0번쨰 인덱스 제외하고 1~N 까지 쓸거기 때문
distance[x] = 0                     # 시작점(출발 도시) 0으로 초기화 하고 시작

way = deque([x])                    # 큐 선언하며 바로 시작점 넣어주기

# count = 0

while way:
    nx = way.popleft()              # 함수 뒤에 () 붙이는 거 잊지 말자
    for next_node in way[nx]:
        if distance[next_node] == -1:
            distance[next_node] = distance[nx]+1
            way.append(next_node)

# 결과 출력
found = False