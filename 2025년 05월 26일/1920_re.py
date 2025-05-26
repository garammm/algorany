# 다시 풀어도 정말^^ 생각 세번 하고 풀기^^
def binary_search(array, target, start, end):
    while start<=end:
        mid = (start+end)//2
        if target<array[mid]:
            end = mid -1
        elif target==array[mid]:
            return target
        else:
            start = mid+1

# 제에바알... 이진 탐색법은 정렬 되어있어야 한다...
n=int(input())
a_list=list(map(int, input().split()))
m=int(input())
b_list=list(map(int, input().split()))
a_list.sort()

for b in b_list:
    if binary_search(a_list, b, 0, n-1):
        print(1)
    else:
        print(0)