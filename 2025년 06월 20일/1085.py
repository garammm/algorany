x, y, w, h = map(int, input().split())

a = min(x,y)
b = min(a,w-x)
c = min(b,h-y)

print(c)