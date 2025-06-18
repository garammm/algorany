# 1966
from collections import deque

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    priority = list(map(int, input().split()))

    q = deque()
    for i in range(n):      # 원래 순서 기억하기 위해서
        q.append((i, priority[i]))

    count =0

    while q:
        cur = q.popleft()
        if any(cur[1] < other[1] for other in q):        # any() 하나라도 참이면 True, 이거 정말 오늘의 배움 그 자체
            q.append(cur)
        else:
            count+=1
            if cur[0]==m:
                print(count)