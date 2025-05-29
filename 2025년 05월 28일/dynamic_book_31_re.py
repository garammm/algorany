t=int(input())
for _ in range(t):
    n,m = map(int, input().split())
    data = list(map(int,input().split()))       # 데이터 2차원 배열로 나눌거면 list로 받자

    gold_map = []
    for i in range(0, n):
        gold_map.append(data[i*m:(i+1)*m])

    
    d = [[0]*m for _ in range(n)]

    for i in range(n):
        d[i][0]=gold_map[i][0]

    # m과 n 순서 모두가 문제인... 
    for j in range(m):
        for i in range(n):
            left_down = d[i+1][j-1] if i+ 1<n else 0
            left = d[i][j-1]
            left_up = d[i-1][j-1] if i>0 else 0

            d[i][j]=gold_map[i][j] + max(left_down, left, left_up)
    answer = []
    for i in range(n):
        answer.append(d[i][m-1])

    print(max(answer))
