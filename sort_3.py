# 퀵 정렬 소스코드(이코테)

array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:            # 원소가 1개인 경우 종료 -> 나중에 다시 한번 체크
        return
    pivot = start
    left = start + 1            # 두번째 데이터부터 시작, 인덱스 번호라는 걸 잊지 않기기
    right = end                 # 마지막 데이터랑

    while left<=right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복(왼쪽은 큰 데이터 찾기)
        while left <= end and array[left] <= array[pivot]:
            left += 1           # 기준보다 작으면 다음

        # 피벗보다 작은 데이터를 작을 때까지 반복(오른쪽은 작은 데이터 찾기)
        while right > start and array[right]:
            right -= 1
        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:    
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else: 
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right -1)
    quick_sort(array, right+1, end)
    
quick_sort(array, 0, len(array)-1)              # 0~9까지 -> 마지막 수 포함..

print(array)
