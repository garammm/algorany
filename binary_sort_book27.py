# 누군가의 잘난척으로 만들어진 코드...
# 아 화나....
#아 짜증....
from bisect import bisect_right, bisect_left
n,x = map(int, input().split())
num_list = list(map(int, input().split()))

left = bisect_left(num_list, x)
right = bisect_right(num_list, x)

count = right - left

if count == 0:
    print(-1)
else:
    print(count)