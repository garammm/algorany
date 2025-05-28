# 이코테 다이나믹 프로그래밍 2번 다시 풀어보기
# 다시 풀어도 정말^^
# 또 다시 푸는 수밖엔..
# 점화식..

x= int(input())

d = [0] * (x+1)

for i in range(2,x+1):
    d[i] = d[i-1]+1      
    if i%5 ==0:
        d[i]=min(d[i],d[i//5]+1)
    elif x%3 == 0:
        d[i]=min(d[i],d[i//3]+1) 
    elif i%2 ==0:
        d[i]=min(d[i],d[i//2]+1) 

print(d[x])