# 2792
# 이해도 필요하고 코드 암기도 필요하고..

n, m = map(int, input().split())
jewels = list(map(int, input().split()))

def count_boxes(capacity):
    total = 0
    for jewel in jewels:
        total += (jewel + capacity - 1) // capacity
    return total

left, right = 1, max(jewels)

while left <= right:
    mid = (left + right) // 2
    if count_boxes(mid) <= m:
        right = mid - 1
    else:
        left = mid + 1

print(left)
