# 이 문제 잘은 모르지만 크루스칼이면 풀 수 있을 것 같아..!
# 일단 코드 가져오고 그 다음에 고쳐보도록 해보자!

from collections import deque

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] =a
    else:
        parent[a]=b

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
parent = [[] for i in range(v+1)]

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()
last = 0            # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선선

# 간선을 하나씩 확인하며 
for edge in edges:
    cost, a, b = edge
    # 싸이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result-last)