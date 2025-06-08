n = int(input())
# 그냥 냅다 데이터 받네..?
graph = [list(map(int,input().split())) for _ in range(n)]

for k in range(n):          # 중간지점
    for i in range(n):      # 시작지점
        for j in range(n):  # 끝나는 지점
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1         # 직접 연결이 아닌 간접 연결도 연결이다~

for row in graph:
    print(*row)                 # 리스트 안의 값들 하나씩 분리해서 출력