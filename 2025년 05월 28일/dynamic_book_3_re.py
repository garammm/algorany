# 이코테 다이나믹 프로그래밍 3번
# 다음날 다시 풀어도 똑같이 못푸는...
# 내일 또다시 풀어보면 되지!

n = int(input())
food_map = list(map(int,input().split()))


d = [0]*(n+1)
d[1] = food_map[0]
d[2]= max(food_map[0], food_map[1])

# max(전의 최댓값이나, 전전의 최댓값에서 이번 값을 더한것)
for i in range(3,n+1):
    d[i] = max(d[i-1], d[i-2] +food_map[i-1])


print(d[n])