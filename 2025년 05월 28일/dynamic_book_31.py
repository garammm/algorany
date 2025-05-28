# 이코테 31. 금광 문제 -> 코드를 보고 이해는 된다. 2차원 리스트 받는 법 다시 한번 복습. 이 문제는 내일 다시 풀어보자!

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())  # 행, 열
    data = list(map(int, input().split()))

    # 금광 정보를 2차원 리스트로 변환 -> 이 부분 기억하기기
    gold = []
    for i in range(n):
        gold.append(data[i * m:(i + 1) * m])

    # DP 테이블 초기화 (금광과 동일 구조) 
    dp = [[0] * m for _ in range(n)]

    # 첫 번째 열은 그대로 복사-> 여기까진 함... 근데 그 다음이 문제다...
    for i in range(n):
        dp[i][0] = gold[i][0]

    # 오른쪽으로 이동하며 dp 테이블 채우기
    for j in range(1, m):  # 열 반복
        for i in range(n):  # 행 반복
            # 왼쪽 위, 왼쪽, 왼쪽 아래 값 확인 -> 오른쪽으로 가나 DP가 누적값이므로 전의 값을 봐야함, if 절로 조건 걸어준다...
            left_up = dp[i - 1][j - 1] if i > 0 else 0
            left = dp[i][j - 1]
            left_down = dp[i + 1][j - 1] if i < n - 1 else 0

            # 현재 위치까지 최대 금 저장
            dp[i][j] = gold[i][j] + max(left, left_up, left_down)

    # 마지막 열에서 가장 큰 값이 결과
    result = max(dp[i][m - 1] for i in range(n))
    print(result)
