# 1966
# 바로 보고 풀진 못했고 이해는 되는... 
# 안보고 다시 적어보자

from collections import deque

t = int(input())  

for _ in range(t):
    n, m = map(int, input().split())  # 문서 개수, 내가 알고 싶은 문서 위치
    priorities = list(map(int, input().split()))  # 각 문서 중요도
    
    q = deque()
    for i in range(n):
        q.append((i, priorities[i]))  # (문서 번호, 중요도)
    
    count = 0  # 인쇄 순서
    
    while q:
        cur = q.popleft()
        if any(cur[1] < other[1] for other in q):  # 이 표현은 진짜 처음봤다...
            q.append(cur)  # 다시 뒤로 보냄
        else:
            count += 1  # 인쇄
            if cur[0] == m:  # 내가 찾는 문서면
                print(count)
                break


