# 시간 복잡도 O(NlogN) -> 요구하는 시간 복잡도보다 높다... bisect 사용 X
'''
from bisect import bisect_left, bisect_right

n = int(input())
num_list = list(map(int, input().split()))

for i in range(n):
    a=bisect_left(num_list,i)
    b=bisect_right(num_list,i)
    if num_list[a] ==a:
        print(a)
    elif num_list[b] == b:
        print(b)
'''

def binary_search(array, start, end):
    if start>end:
        return -1                       # 먼저 종료 조건 확인해야함... 뒤에서 X
    mid = (start + end)//2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        end = mid-1
        return binary_search(array, start, end)
    elif array[mid] <mid:
        start = mid + 1
        return binary_search(array, start, end)
    

n = int(input())
num_list = list(map(int, input().split()))
a = len(num_list)

answer = binary_search(num_list, 0, n-1)              # 인덱스 초과 할 수 있으므로 0~n-1로 정리
print(answer)
