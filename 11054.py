n = int(input())
array = list(map(int,input().split()))
dp1 = [1]*n             # 증가하는 수열
dp2=[1]*n               # 감소하는 수열

# 증가 수열
for i in range(n):
    for j in range(i):
        if array[j]<array[i]:
            dp1[i]=max(dp1[i], dp1[j]+1)

# 뒤에서 부터 증가 수열 찾기
for i in range(n-1, -1, -1):             # n-1부터 0까지
    for j in range(n-1, i, -1):
        if array[j]<array[i]:           # i가 순번상 더 앞쪽이니까..
            dp2[i]=max(dp2[i], dp2[j]+1)
answer =0
for i in range(n):
    total = dp1[i]+dp2[i] -1
    answer=max(total, answer)

print(answer)
    