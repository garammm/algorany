# 알고리즘 스터디 정렬 부분 문제
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    if numbers[0] == '0':
        return '0'
        
    answer = ''.join(numbers)
    return answer