from collections import defaultdict

n, k = map(int, input().split())
word_list = []
char_score = defaultdict(int)
default = set('antic')

# 1. 입력 단어 처리
for _ in range(n):
    raw = input().strip()
    for ch in default:
        raw = raw.replace(ch, '')
    word_set = set(raw)
    word_list.append(word_set)

# 2. max_len 계산
max_len = max((len(word_set) for word_set in word_list), default=0)

# 3. 문자 점수 계산
for word_set in word_list:
    priority = max_len - len(word_set) + 1
    for ch in word_set:
        char_score[ch] += priority

# 4. 점수 높은 문자 선택
sorted_chars = sorted(char_score.items(), key=lambda x: -x[1])
selected = set([ch for ch, _ in sorted_chars[:k - 5]])

# 5. 읽을 수 있는 단어 수 계산
readable = 0
for word_set in word_list:
    if word_set <= selected:
        readable += 1
if k < 5:
    print(0)
    exit()

print(readable)
