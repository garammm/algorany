m,n,k = map(int, input().split())
graph=([False] for _ in range(m))
empty = ([False]*n for _ in range(m))

for _ in range(k):
    a,b,c,d = (map(int,input().split()) )
    graph[a].append(b)
    graph[c].append(d)
    for i in range(a,c,1):
        for j in range(b,d,1):
            empty[i][j] += 1


print(empty)



