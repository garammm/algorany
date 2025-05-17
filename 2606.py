n=int(input())
m=int(input())
edges = [tuple(map(int,input().split())) for _ in range(m)]

graph =[[] for _ in range(n+1)]
for a,b in edges:
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)