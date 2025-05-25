# 예시코드로 일단 이해...
n, m = list(map(int, input().split()))
dduk = list(map(int,input().split()))

start = 0 
end = max(dduk)

while(start<=end):
    total = 0
    mid = (start + end) // 2
    for x in dduk:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid        # 가운데를 기준으로 자른다
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end =mid-1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid                # 최대한 덜 잘랐을 때가 정답
        start = mid+1

print(result)
