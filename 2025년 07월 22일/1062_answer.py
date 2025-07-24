# 나중에 다시 풀어보기... 다시 풀 수 있으려나..
from itertools import combinations

n, k = map(int, input().split())
required = set('antic')  # 반드시 배워야 하는 기본 문자
words = []

# k < 5면 기본 문자도 못 배우므로 단어를 하나도 못 읽음
if k < 5:
    print(0)
    exit()

# 단어 입력 처리
all_chars = set()
for _ in range(n):
    word = input().strip()
    remain = set(word) - required
    words.append(remain)
    all_chars.update(remain)

# 만약 배울 수 있는 알파벳이 남은 모든 문자보다 많다면 전부 읽을 수 있음
if k == 26 or len(all_chars) <= (k - 5):
    print(n)
    exit()

# 가능한 모든 조합을 탐색하여 최대 읽을 수 있는 단어 수 계산
max_count = 0
for comb in combinations(all_chars, k - 5):
    learned = set(comb) | required
    count = sum(1 for w in words if w <= learned)
    max_count = max(max_count, count)

print(max_count)
