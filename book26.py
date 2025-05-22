# 이코테-정렬-26. 카드 정렬하기
'''
n=int(input())
card_list = list(int(input()) for _ in range(n))
card_sum=0
card_list.sort()

for i in range(1,n):
    card_sum = card_sum + card_list[i-1]


print(card_sum)
'''

# 정답 코드 with chat gpt
# heapq는 큐에서 최솟값 원소를 출력하게 도와줌
import heapq

n=int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))          # 입력값 받기
    
total = 0

while len(heap)>1:
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)
    sum_ab= a+b
    total += sum_ab
    heapq.heappush(heap,sum_ab)

print(total)
