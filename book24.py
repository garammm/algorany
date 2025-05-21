# 이코테-정렬-24. 안테나
# 내가 생각한 방법 -> 모든 거리를 다 구해본다.
# 시간 복잡도.... 를 고려하지 않음.
# 따라서 문제 푸는 방법: 좌표값들을 정렬한 후 중간 값을 구한다 -> 이것이 최소값
'''
n = int(input())
houses = list(map(int, input().split()))
distance_sum = []
answer = []


for i in range(n): 
    distance_sum = []                                             # 매 i 마다 distance 초기화시켜줘야함
    for j in range(n):
        distance_sum.append(abs(houses[i]-houses[j]))
    answer.append((sum(distance_sum),i))


a,b =min(answer)
print(houses[b])        
'''
# 정답 코드드

n = int(input())
houses = list(map(int, input().split()))
houses.sort()

# 중간값 출력(짝수일 경우에는 더 작은 쪽을 선택)
print(houses[(n-1)//2])         # 짝수 작은 쪽 선택 때문에 (n-1)//2