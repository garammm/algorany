# 백준 1032 명령 프롬프트
# chat gpt의 도움을 꽤나 많이 받아서 푼...


n = int(input())
words = []
for i in range(n):
    words.append(input())

b = len(words[0])

answer =[]

for i in range(b):
    char = words[0][i]
    for j in range(1,n):            # 첫번째는 이미 비교 하고 있으니까 제외
        if words[j][i]!= char:
            char = '?'
            break
    answer.append(char)

print(''.join(answer))