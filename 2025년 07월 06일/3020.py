'''
n,h = map(int,input().split())
cave = []
cave[n+1][h+1] = '0'
for i in range(h):
    stone = int(input())
    if i%2==0:
        for j in range(stone):
            cave[i][j] = 1
    elif i%2==1:
        for k in range(stone):
            cave[i][-k] = 1
sum=0
for p in range(h):
    for j in range(n):
        sum+=cave[p][j]
'''

import sys
import bisect

n, h = map(int, sys.stdin.readline().split())
bottoms = []
tops = []

for i in range(n):
    size = int(sys.stdin.readline())
    if i % 2 == 0:
        bottoms.append(size)
    else:
        tops.append(size)

bottoms.sort()
tops.sort()

min_obstacles = n + 1
count = 0

for height in range(1, h + 1):
    # 석순 장애물 개수
    bottom_idx = bisect.bisect_left(bottoms, height)
    bottom_cnt = len(bottoms) - bottom_idx

    # 종유석 장애물 개수
    top_idx = bisect.bisect_left(tops, h - height + 1)
    top_cnt = len(tops) - top_idx

    total = bottom_cnt + top_cnt

    if total < min_obstacles:
        min_obstacles = total
        count = 1
    elif total == min_obstacles:
        count += 1

print(min_obstacles, count)
