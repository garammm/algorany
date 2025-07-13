s=input()
t=input()

s_length = len(s)
t_length = len(t)

for _ in range(t_length - s_length):
    if t[-1]=="A":
        t=t[:-1]
    elif t[-1]=='B':
        t=t[:-1]
        t=t[::-1]
    
if t == s:
    print("1")
elif t != s:
    print("0")