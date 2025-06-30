n=int(input())
card=list(map(int,input().split()))

answer = [0]*(n+1)
answer[1]=card[0]
answer[2]=max(answer[1]+answer[1], card[1])

for i in range(3,n+1):
    answer[i]=card[i-1]
    for j in range(i):
        answer[i]=max(answer[j]+answer[i-j], answer[i])
    
print(answer[n])