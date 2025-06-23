string = input()
a = len(string)

count_left = 0
count_right = 0
answer_count = 0
stack = [] 

for char in string:
    if char == '{':
        stack.append(char)
    else:                           # 닫는 괄호일 경우
        if stack:                   # stack에 뭔가 있을 때
            stack.pop()
        else:
            pass
        