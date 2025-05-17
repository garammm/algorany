a = int(input())
scores = list(map(int, input().split()))

scores.sort()
new_scores=[]

for n in range(a):
    new_score=scores[n]/scores[a-1]*100
    new_scores.append(new_score)

avg = sum(new_scores)/a
print(avg)
