
t = int(input())
for _ in range(t):
    n = int(input())
    clothes = []
    for _ in range(n):
        cloth, jong = map(str, input().split())
        clothes.append((cloth, jong))
    counts={}
    for cloth, jong in clothes:
        if jong in counts:
            counts[jong]+=1
        else:
            counts[jong]=1
    
    answer =1
    for count in counts.values():
        answer *= (count+1)
    print(answer-1)
