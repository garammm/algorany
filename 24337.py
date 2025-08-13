n, a, b = map(int, input().split())

if a+b-1<=n:
    num_list = [1]*n
    gap = n - (a + b - 1)
    if a==1:
        num_list[0] = max(a,b)

        for i in range(b-1):
            num_list[n-b+1+i]=b-1-i
    elif b==1:
        num_list[-1]=max(a,b)
        for i in range(a-1):
            num_list[gap+i]=i+1
    else:
        for i in range(a-1):
            num_list[gap + i] = i + 1
        num_list[gap+a-1]=max(a,b)
        
        for i in range(b-1):
            num_list[n-b+1+i]=b-1-i

    print(*num_list)
else:
    print(-1)