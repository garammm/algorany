def answer(string):
    stack = [] 

    for char in string:
        if char == '{':
            stack.append(char)
        elif char == '}':
            if stack:                   # stack에 뭔가 있을 때
                stack.pop()
            else:
                stack.append(char)
                pass          # 짝이 안맞으면 일단 stack에 넣는다.

    a = len(stack)
    count_left = 0
    count_right = 0
    if a ==0:
        return 0 

    for char in stack:   
        if char == "{":
            count_left +=1
        elif char == "}":
            count_right+=1

    # 2,4 까지 고려하고 6일 때를 고려하지 않음
    '''
    if count_right %2 ==1:
        return (int(a//2+1))
    else:
        return (int(a//2))
        '''
    return (count_left +1)//2 + (count_right+1)//2

test_case = 1
while True:
    # 문자열에서 오른쪽 끝 부분에 있는 공백 문자들을 제거할 때 쓰느 함수
    string = input().rstrip()     
    if string[0] == '-':   # 종료 조건
        break
    result = answer(string)
    # 테스트케이스 번호. 답 형식으로 출력해야 하므로
    print(f"{test_case}. {result}")
    test_case += 1