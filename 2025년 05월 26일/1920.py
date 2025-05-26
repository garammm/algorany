# 꼭 다시 풀어보기...아니다 이건 꼭... 내일 아침에 다시 꼭 다시... 피티 없이 풀어보자...
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return False

n = int(input())
a_list = list(map(int,input().split()))
m = int(input())
b_list = list(map(int,input().split()))

a_list.sort()


for b in b_list:
    if binary_search(a_list, b, 0, n-1):
        print(1)
    else:
        print(0)