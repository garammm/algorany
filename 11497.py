t = int(input())
for _ in range(t):
    n=int(input())
    tree=[]
    tree=list(map(int, input().split()))
    tree.sort()

    answer=[]
    for i in range(n-2):
        answer.append(abs(tree[i]-tree[i+2]))
    answer.append(abs(tree[0]-tree[1]))
    answer.append(abs(tree[n-1]-tree[n-2]))

    real_answer= max(answer)
    print(real_answer)
