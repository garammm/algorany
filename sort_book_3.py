# 정렬 - 실전문제 4. 두 배열의 원소 교체
# 내 코드... 너무 복잡하게 생각함함
'''
n,k = map(int,input().split())                  # n은 원소 개수, k는 최대 횟수
a_array = list(map(int,input().split()))
b_array = list(map(int,input().split()))

a_array.sort(reverse=True)
b_array.sort(reverse=True)
count = 0 

while k:
    if a_array[n-1] >= b_array[0]:
        quit()
    
    for i in range(n):
        for j in range(n):
            if a_array[n-j]< b_array[i]:
                a_array[n-j], b_array[i] = b_array[i], a_array[n-j] 
                count += 1
            if count > k:
                quit()

answer = sum(a_array)
print(answer)
'''

# 정답 코드

n,k = map(int,input().split())                  # n은 원소 개수, k는 최대 횟수
a_array = list(map(int,input().split()))
b_array = list(map(int,input().split()))

a_array.sort()                      # a 배열은 오름차순, b 배열은 내림차순
b_array.sort(reverse=True)          # a 배열의 가장 작은 수가 b 배열의 가장 큰 수보다 작다면 바꾼다. -> 아이디어

for i in range(k):
    if a_array[i] < b_array[i]:
        a_array[i], b_array[i] = b_array[i], a_array[i]
    else:
        break                   # 내가 복잡하게 생각했던 b배열의 가장 큰수 어쩌고 저쩌고... 그냥 break 하기

print(sum(a_array))
