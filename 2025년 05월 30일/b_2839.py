# 백준 2839 설탕 배달달
n = int(input())

# 런타임 에러나지 않도록 -1로 초깃값 설정정
d = [-1] * 5001

d[3]=1
d[5]=1

# 변수 제대로 적었나 확인... 꼭...
# 런타임 에러난다..
for i in range(6, n+1):
    if d[i-3] != -1 and d[i-5] != -1:
        d[i] = min(d[i-3], d[i-5])+1
    elif d[i-3] == -1 and d[i-5] != -1:
        d[i]=d[i-5]+1
    elif d[i-5] == -1 and d[i-3] != -1:
        d[i]=d[i-3]+1
    else:
        d[i] = -1

print(d[n])

    