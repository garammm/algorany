a=int(input())
atm_line = list(map(int,input().split()))
atm_line.sort()
total = 0
atm_sum=0

for i in range(a):
   total +=  atm_line[i]
   atm_sum += total

print(atm_sum)