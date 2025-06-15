# 알고리즘 스터디 
# 26091번 현대모비스 소프트웨어 아카데미

# 이 문제 보자마자 어디서 본것 같은 생각이 바로 들고 막 그래
# 뭐지 왜 익숙해

# 헐 해냄
# 투 포인터 기억 안나서 투 포인터 예시 코드 보고 바로 해냄
# 그리고 투 포인터로 푼다는 거 보자마자 바로 캐치해냄
# 오 좀 더 나아짐!

n, m = map(int, input().split())
ability=list(map(int,input().split()))


ability.sort()      # 내림차순
count = 0           


left = 0 
right = n -1

while left<right:
    total = ability[left] + ability[right]
    
    if total >= m:
        count +=1
        left +=1
        right -=1
    elif total < m:
        left +=1
    
print(count)