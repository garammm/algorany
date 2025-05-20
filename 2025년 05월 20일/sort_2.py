# 삽입 정렬 소스코드(이코테)

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    # 어디에 삽입될 것인지 위치 보기 위한 코드
    for j in range(i,0,-1):
        if array[j]<array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]          
        else:
            break
print(array)