'''
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def dfs(start):
    visited = [0] * (n+1)
    stack = [start]
    visited[start]=True     # 시작점 방문
    count =1                # 자기 자신 포함

    while stack:
        node=stack.pop()
        for neighbor in graph[node]:
            if visited[neighbor]==0:
                visited[neighbor]=True
                count+=1
                stack.append(neighbor)
    return count

real_answer=0
answer_list = []
for i in range(1,n+1):
    answer = dfs(i)
    answer_list.append(answer)
    real_answer=max(answer,real_answer)

for i in range(n):
    if answer_list[i]==real_answer:
        print(i+1, end = ' ')
    
'''
# 답
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)  # B → A 방향

def bfs(start):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                count += 1
                queue.append(neighbor)
    return count

max_hack = 0
result = []

for i in range(1, n + 1):
    hacked = bfs(i)
    if hacked > max_hack:
        max_hack = hacked
        result = [i]
    elif hacked == max_hack:
        result.append(i)

print(*result)
