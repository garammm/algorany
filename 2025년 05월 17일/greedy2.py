# 큰 수의 법칙(그리디 실전문제 2)
n, m, k = map(int,input().split())
n_list=list(map(int,input().split()))

n_list.sort()
first = n_list[n-1]
second = n_list[n-2]

# 큰 수가 더해지는 횟수
count_first = m*k/(k+1) + m%(k+1)

# 작은 수가 더해지는 횟수
count_second = m/(k+1)

# 총 합
total = int(first * count_first + second * count_second)

print(total)

# 오... 해결