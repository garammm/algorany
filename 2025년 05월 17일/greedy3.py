# Greedy 3번 문제 -> 책에 있는 정답 코드 그러나 이해함! 그리고 스스로 적어봄!(안보고!!)
n,m = map(int,input().split())

answer = 0
for _ in range(n):
    n_list = list(map(int, input().split()))
    min_num = min(n_list)
    answer = max(min_num, answer)

print(answer)