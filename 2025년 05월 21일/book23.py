# 이코테-정렬-23. 국영수
# 한 줄 정리. lambda, sort 이런식으로 쓰는거 처음 암... 그리고 이젠 기억해야 해해

n = int(input())
student =[]

for _ in range(n):
    input_data = input().split()
    student.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))             # append 할때 (()) 잊지 않기

### 잊지 않아야 할 개념 ###
student.sort(key = lambda x:(-x[1],x[2],-x[3],x[0]))

### 간단한데 생각이 안나는 부분 ###
for student_name in student:
    print(student_name[0])