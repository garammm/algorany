t = int(input())
for _ in range(t):
    n = int(input())
    employee=[]
    for _ in range(n):
        a, b = map(int, input().split())
        employee.append((a,b))
    employee.sort(key=lambda x : x[0])

    count = 1
    best_interview = employee[0][1]

    for i in range(1, n):
        # 면접 성적이 지금까지 중 최고일 경우만 선발
        if employee[i][1] < best_interview:
            count += 1
            best_interview = employee[i][1]

    print(count)
