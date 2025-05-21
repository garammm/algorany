# 계수 정렬 소스코드 (이코테)

array = [7,5,9,0,3,1,6,2,4,8,0,5,2]

# 모든 범위를 포함하는 리스트 선언(모든 값을 0으로 초기화)
count = [0] * (max(array)+1)        # 인덱스 0때매 포함

for i in range(len(array)):
    count[array[i]] += 1            # 각 데이터에 해당하는 인덱스 값 증가


for i in range(len(count)):
    for j in range(count[i]):       # 개수 만큼 출력
        print(i, end=' ')           # 띄어쓰기로 구분