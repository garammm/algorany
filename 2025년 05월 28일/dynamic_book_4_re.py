# 이코테 다이나믹 프로그래밍 4번
# 드디어 오늘 처음으로 다시푼 문제 맞음!
# ㅎㅎㅎㅎㅎㅎㅎㅎ

n = int(input())

d = [0]*(n+1)

d[1]=1
d[2]=3

for i in range(3,n+1):
    d[i] = (2*d[i-2] + d[i-1])%796796

print(d[n])