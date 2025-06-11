# 그래프 이론
# 2번 실전 문제 팀 결성
# 처음치고 제법 정답에 가깝게 갔으니까 다음번에 한번 더 하면 제대로 할 수 있을지도..?

# 서로소 문제니까 find parent 함수 만들기
def find_parent(parent, z):
    if parent[z] != z:
        parent[z] = find_parent(parent, parent[z])
    return parent[z]

# 서로소 문제니까 union 함수 만들기기
def union(parent, x, y):
    x = find_parent(parent, y)
    y = find_parent(parent, x)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().split())
parent = [0]*(n+1) 


for _ in range(m):
    what, a, b = map(int, input().split())
    if what == 0:
        union(parent, a, b)
    elif what == 1:
        if find_parent(parent, a)==find_parent(parent, b):
            print("YES")
        else:
            print("NO")