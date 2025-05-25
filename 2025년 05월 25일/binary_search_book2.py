'''
# 내 풀이
n = int(input())
stores = list(map(int, input().split()))
m = int(input())
want = list(map(int, input().split()))

for stuff in want:
    if stuff in stores:
        print("yes")
    else:
        print("no")


# 다른 풀이들(이진 탐색 알고리즘)
def binary_search(array, target, start, end):
    while start <=end:
        mid = (start+end)//2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽
        elif array[mid] > target:
            end = mid-1
        # 중간점의 값보다 찾고자 한느 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# 입력값들 입력 받기
n = int(input())
array = list(map(int,input().split()))
array.sort()        # 이진 탐색을 위한 정렬
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end = ' ')

'''
'''
# 계수 정렬 
# 가게의 부품 개수 입력 받기
n = int(input())            
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1

# 요청 부품 개수 입력받기
m = int(input())
x = list(map(int,input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
'''


