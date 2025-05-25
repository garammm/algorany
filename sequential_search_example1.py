# 순차 탐색 소스 코드 구현
def sequential_search(n, target, array):
    for i in range(n):
        # 각 원소를 하나씩 확인하며
        if array[i] == target:
            return i+1                              # 현재의 위치 반환(인덱스는 0부터 시작하니까 +1

input_data = input().split()
n = int(input_data[0])  # 원소의 개수
target = input_data[1]  # 찾고자 하는 문자열
array = input().split()

print(sequential_search(n,target,array))            # 결과 출력