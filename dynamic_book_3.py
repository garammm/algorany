# 개미전사~
# 이코테 다이나믹 프로그래밍 3번

n = int(input())
food_map = list(map(int, input().split()))

d = [0]*(n+1)

# 다이나믹 프로그래밍(bottom-up), 0, 1을 정하고, 점화식을 세워서 생각하는게... 
d[0] = food_map[0]
d[1] = max(food_map[0], food_map[1])
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2]+food_map[i])

print(d[n-1])                   # 마지막 집의 index: n-1
