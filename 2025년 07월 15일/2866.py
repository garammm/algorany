# 이 문제는 나중에 다시 풀어보기
n,m = map(int, input().split())
word_list = [list(input()) for _ in range(n)]
new_list = []

for j in range(m):
    for i in range(1,n):
        new_list.append(word_list[i][j])

def is_unique(start_row):
    col_words=set()
    for col in range(m):
        word=''.join(word_list[row][col] for row in range(start_row, n))
        if word in col_words:
            return False
        col_words.add(word)
    return True

left = 0
right = n-1
answer = 0
while left <= right:
    mid = (left+right)//2
    if is_unique(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)