from itertools import combinations
import sys
input = sys.stdin.read

data = input().split()
n = int(data[0])
k = int(data[1])
words = data[2:]

# 기본적으로 반드시 배워야 하는 5글자
required = set('antic')

# 배울 수 있는 글자가 5보다 작으면 어떤 단어도 못 읽음
if k < 5:
    print(0)
    exit()

# 단어들에서 기본 문자 제외 후 남은 알파벳만 추림
processed_words = []
all_chars = set()

for word in words:
    unique = set(word) - required
    processed_words.append(unique)
    all_chars.update(unique)

# 배울 수 있는 나머지 글자 수
rest = k - 5

# 가르칠 수 있는 모든 조합 중 최대 읽을 수 있는 단어 수 찾기
max_count = 0

# 예외: 가르칠 수 있는 알파벳이 남은 모든 알파벳 이상이면 전부 읽힘
if len(all_chars) <= rest:
    print(n)
    exit()

# 모든 가능한 조합 순회
for comb in combinations(all_chars, rest):
    teach = set(comb)
    count = 0
    for word_chars in processed_words:
        if word_chars <= teach:
            count += 1
    max_count = max(max_count, count)

print(max_count)
