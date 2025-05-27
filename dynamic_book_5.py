# 효율적인 화폐구성
# 이코테 다이나믹 프로그래밍 5번번

n, m = map(int, input().split())
money_list = list(int(input()) for _ in range(n))

# 최솟값을 구하므로 비교해서 초기값 탈락하기 쉽도록 가장 큰수를 넣는다.
dp = [10001] *(m+1)
dp[0] =0

# 대충 무슨 말인지는 알겠는데 정확히는 모르겠는...
for coin in money_list:
    for x in range(coin, m+1):
        if dp[x-coin]!=10001:
            dp[x]=min(dp[x], dp[x-coin]+1)              

print(dp[m] if dp[m] != 10001 else -1)