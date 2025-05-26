# 이코테 29 공유기 설치치
# 나중에 다시 풀어보자... 이유는 다시 풀어도 못 풀 것 같아..
n, c = map(int, input().split())
house = list((int(input())) for _ in range(n))

start = 1       # 최솟값값
end = house[-1]-house[0]        #최댓값값
result = 0

while(start<=end):
    mid =(start+end)//2         # mid는 가장 인접한 두 공유기 사이의 거리(gap)을 의미
    value = house[0]
    count = 1

    # 현재의 mid 값을 이용해 공유기를 설치 -> 이해 X
    for i in range(1,n):
        if house[i] >= value + mid:
            value = house[i]
            count+=1
    if count >= c:
        start = mid +1              # 최솟값에 1 더한것
        result = mid
    else:
        end = mid -1

print(result)