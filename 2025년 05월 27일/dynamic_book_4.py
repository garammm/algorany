# 바닥공사
# 이코테 다이나믹 프로그래밍 4번
# 내가봤을 떈 점화식 세우고, 초기 항만 잘 설정 해놓으면 큰 문제없이 풀려...
# 근데 그 점화식이 아리송한게...

n = int(input())

d = [0] * 1000


d[1] = 1
d[2] = 3             

for i in range(3, n+1):
    d[i] = (d[i-1]+2*d[i-2]) % 796796

print(d[n])