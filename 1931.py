a=int(input())
during_times =[]
during = 0
for _ in range(a):
    start, end = tuple(map(int,input().split()))
    during = end-start
    during_times.append((during, end))

# 튜플 두번쨰 요소로 정렬
during_times.sort(key = lambda x:x[1])

print(during_times)







