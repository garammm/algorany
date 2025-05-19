m,n,k = map(int, input().split())
li = (list(map(int, input().split())) for _ in range(2*k))

empty = ([False]*n for _ in range(m))

def DFS(x):
    empty[]