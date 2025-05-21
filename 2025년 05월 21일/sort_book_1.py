# 정렬 - 실전문제 2. 위에서 아래로

n = int(input())

num_list =[]
for _ in range(n):
    num_list.append(int(input()))                     # 데이터 받는거 나중에 다시 해보기

num_list.sort(reverse = True)                         # 그냥 적지 말고 reverse = True로 해야 오름차순으로 할 수 있음음

for i in num_list:
    print(i, end=' ')