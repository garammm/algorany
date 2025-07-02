# 이진탐색은 나중에 꼭 다시 풀어보자...
import math

try:
    n, m = map(int, input().split()) # n 보석 개수, 친구수 m
    jewels = []
    for _ in range(n):
        jewels.append(int(input()))
except EOFError:
    # 입력이 없으면 종료
    exit(0)

# 이 부분이 특이하다
def binary_search(jewels, max_per_friend, m):
    count = 0
    for jewel in jewels:
        # 각 상자를 max_per_friend 개씩 나눌 떄 필요한 친구 수
        count += math.ceil(jewel/max_per_friend)
    return count <= m
    
start = 1
end = max(jewels)
result = end

while start <= end:
    mid = (start + end)//2
    if binary_search(jewels, mid, m):
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)