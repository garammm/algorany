name = input()
name_length = len(name)
count =0

for c in name:
    num_c = ord(c)
    if num_c <= ord('M'):
        count += (num_c - ord('A'))
    elif num_c <= ord('N'):
        count += (ord('N')-num_c)
        
answer = count + name_length -1

print(answer)

# 첫번째 질문. 이게 왜 그리디이지..? 
# 두번째 질문. 왜 안돌아가지..?
