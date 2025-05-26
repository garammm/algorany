# 알고리즘 스터디_이분탐색 문제
# 나중에 꼬옥 다시 풀어보기
level = int(input())
slime_list = list(int(input()) for _ in range(level))

result =0
'''
def binary_search(target, start, end):
    mid= (start+end)//2
    if start>end:
        return mid
    
    if mid>target:
        end=mid-1
        return binary_search(target, start, mid-1)
    elif mid< target:
        start=mid+1
        return binary_search(target, mid+1, end)
    elif mid == target:
        return mid
'''

def binary_search(target, start, end):
    result = end        # 최댓값부터 시작-> 근데 왜?
    while start<=end:
        mid = (start+end)//2
        if mid * (mid+1) > target:
            result = mid
            end = mid -1
        else:
            start=mid +1
    return result

answer =[]
for i in range(level):
    slime_score =0
    a = slime_list[i]           # 슬라임 n마리
    slime_score = a*(a+1)//2     
    answer.append(binary_search(slime_score, 0, 1000000000))  
    
    
for real in answer:
    print(real)
                