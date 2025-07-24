import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())        # 집, 다리
s, e = map(int, input().split())        # 시작, 끝

cebu_map = [[] for _ in range(n+1)]
maximum = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    # 양방향 그래프
    cebu_map[a].append((b,c))
    cebu_map[b].append((a,c))
    if maximum<c:
        maximum=c



def bfs(limit):
    visited = [False] * (n+1)
    queue = deque()
    queue.append(s)
    visited[s] = True

    while queue:
        current = queue.popleft()
        for neighbor, weight in cebu_map[current]:
            if visited[neighbor]==0 and weight>=limit:
                visited[neighbor]=True
                queue.append(neighbor)
    return visited[e]

left = 1
right = maximum
answer=0
while left <= right:
    mid=(left+right)//2
    if bfs(mid)==1:
        answer=mid
        left=mid+1
    else:
        right=mid-1

print(answer)

