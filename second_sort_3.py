n = int(input())
stu_list =[]


for _ in range(n):
    #data_input = map(str, input().split())
    data_input=input().split()
    stu_list.append(((data_input[0]), int(data_input[1])))              # 한덩어리로 묶은 걸 괄호에 넣는다고 생각하자자

stu_list.sort(key = lambda x:x[1])

#print(stu_list[0] for _ in range(n))
for x in stu_list:                                                      # 이 부분 다시 체크크
    print(x[0])