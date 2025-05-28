# 이코테 다이나믹 프로그래밍 5번 다시 풀기
n,m = map(int,input().split())
money_list=list(int(input()) for _ in range(n))

d = [10001]*(m+1)
d[0]=0

# 어제보다 나아진 점. 이제 정확히 무슨 말인지는 안다. 근데 다시 못풀겠을 뿐..
# 낼 다시 풀어보자
for i in range(n):
    for j in range(money_list[i], m+1):
        if d[j-money_list[i]] != 10001:
            d[j] = min(d[j], d[j-money_list[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

