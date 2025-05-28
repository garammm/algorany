t=int(input())
for _ in range(t):
    n,m = map(int, input().split())
    data = map(int,input().split())

    gold_map = []
    for i in range(0, n):
        gold_map.append(data[i*m:(i+1)*m])

    
    d = [[0]*m for _ in range(n)]

    for i in range(n):
        d[0][i]=gold_map(0,i)

    for i in range(n):
        for j in range(m):
            left_down = d[i-1][j-1] if i-1 > 0 else 0
            left = d[i-1][j]
            left_up = d[i+1][j-1] if i+ 1<n else 0

            d[i][j]=gold_map[i][j] + max(left_down, left, left_up)
    answer = []
    for i in range(n):
        answer.append(d[i][m])

    print(max(answer))

