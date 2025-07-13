import sys
from collections import deque

input = sys.stdin.readline
ans = []

while True:
    input_str = list(input().rstrip())
    if input_str[0] == '-':
        break

    str = deque() # 불완전한 괄호쌍들만 남기기
    cnt = 0 # 연산 횟수

    for i in range(len(input_str)):
        if input_str[i] == '{':
            str.append('{')
        else: # 문자가 '}' 라면
            if len(str) > 0 and str[-1] == '{':
                str.pop()
            else:
                str.append('}')

    # str에서 연산 횟수 구하기
    if len(str) == 0:
        cnt = 0
    else:
        for i in range(0, len(str)-1, 2):
            # str에는 원소가 짝수 개만 남았을 것이고
            # {{, }}, }{ 세 가지 경우가 있을 것임
            if str[i] == str[i+1]:
                cnt += 1
            else:
                cnt += 2

    ans.append(cnt)

for i in range(len(ans)):
    print(i+1, end='. ')
    print(ans[i])