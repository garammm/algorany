# 정렬 - 실전문제 3. 성적이 낮은 순서로 학생 출력하기
# 형식을 모르겠는 부분이라 나중에 다시 꼭 풀어보기..!

n = int(input())

student_list = []

# 이 부분 기억...
for _ in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장(*)
    student_list.append((input_data[0], int(input_data[1])))

# 키(key)를 이용하여 점수를 기준으로 정렬 -> 이거 꼭 외우자..
student_list.sort(key = lambda x:x[1])

for x in student_list:
    print(x[0], end = ' ')
