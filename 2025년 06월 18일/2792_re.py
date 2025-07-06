# 너무 답답한 나머지 구글링 시작...
# 지금은 어케저케 이해는 했는데 이거 나중에 다시 풀어보자 어렵다..

import sys
input = sys.stdin.readline          # 메모리 줄임

n,m = map(int, input().split())     # n이 학생, m이 색상
jewerls = []

for i in range(m):
    jewerls.append(int(input()))

start = 1                           
end = max(jewerls)
answer = 0

while start<=end:
    mid = (start+end)//2
    sum = 0
    for i in range(len(jewerls)):
        sum+=jewerls[i]//mid
        if jewerls[i]//mid:
            sum += 1
    if sum > n:
        start = mid+1
    else:
        end=mid-1
        answer=mid
print(answer)

