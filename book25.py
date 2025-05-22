# 이코테-정렬-25. 실패율
# 나 왜 실패율을 안넣고 다 풀었다고 생각하고 있었지..?
'''
def solution(N, stages):
    stages_list = [[] for _ in range(N+1)]                                          # 왜 2인지 아직..
    for i in range(N+1):
        count = 0
        for j in range(len(stages)):
            if i == stages[j]:
                count += 1
            stages_list[i].append((i, count))
    
    stages_list.sort(key = lambda stages:stages[1], reverse = True)              # .sort 이제는 기억하자... 
        
    return stages_list
'''

#예시 입력값
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]



def solution(N, stages):
    stages_list =[]         # (스테이지 번호, 실패율) 저장할 리스트
    total = len(stages)     # 총 도전자 수

    for i in range(1, N+1):
        count = stages.count(i)     # i 스테이지에 머무른 인원수

        if total == 0:
            failure = 0
        else:
            failure = count / total

        stages_list.append([i,failure])     # 구한 값 리스트에 저장

        total -= count                      # 다음 스테이지로 넘어감

    # 실패율 기준으론 내림차순, 같은 실패율일 때 스테이지 번호는 오름차순
    stages_list.sort(key=lambda x:(-x[1], x[0]))
    
    # 2차원 리스트(리스트 안에 리스트)에서 각 서브 리스트의 첫 번째 값만 뽑아 새로운 리스트로 만든다
    return [i[0] for i in stages_list]

answer=solution(N, stages)
print(answer)