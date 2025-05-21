# 파이썬의 장점을 살려 작성한 퀵 정렬 소스코드 (이코테)
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]            # 첫번쨰 원소 기준으로
    tail = array[1:]

    left_side = [x for x in tail if x<= pivot]
    right_side = [x for x in tail if x > pivot]

    # 분할 마친 왼쪽, 기준, 오른쪽 다시 정렬 해서 리스트 반환
    return quick_sort(left_side)+ [pivot] + quick_sort(right_side)      # 리스트들끼리 합칠 수 있으므로 [pivot]

print(quick_sort(array))