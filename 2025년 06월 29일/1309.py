n = int(input())
r=1
l=1
x=1

for i in range(1,n):
    r_a = (l+x)%9901
    l_a = (r+x)%9901
    x_a = (r+l+x)%9901

    r=r_a
    l=l_a
    x=x_a


print((r+l+x)%9901)