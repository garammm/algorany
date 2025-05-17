# 실력이 늘고 다시 오겠습니다.

shortboy=[]
duhagi = 0

for i in range(9):
    a= int(input())
    shortboy.append(a)

total = sum(shortboy)

for i in range(7):
    duhagi += shortboy[0] 
    
    if duhagi<100:
        duhagi -= shortboy[i]
        for i in range(7,9):
            duhagi += shortboy[i]
            if duhagi == 100:
                print (i)