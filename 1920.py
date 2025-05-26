
n = int(input())
a_list = list(map(int,input().split()))
m = int(input())
b_list = list(map(int,input().split()))

a_list.sort()
b_list.sort()

for a in a_list:
    for b in b_list:
        if b==a:
            print("1")
        elif b!=a:
            print("0")