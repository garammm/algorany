from collections import deque

n, m = map(int, input().split())    # n이 가로, m이 세로
tomato_map=[]
for _ in range(m):
    tomato_map=list(map(int,input()))
   
def dfs(x,y):
    if x<-1 or y<-1 or x>=m or y>=n:
        return False
    if tomato_map(x,y)==1:
        tomato_map(x+1, y) = 1
        tomato_map(x,y+1) =1
        tomato_map(x-1,y)=1
        tomato_map(x,y-1)=1
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
        return True
    return False

