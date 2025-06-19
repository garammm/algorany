a = int(input())
b = int(input())

answer1=a*(b%10)
answer2=a*(b%100-b%10)/10
answer3=a*(b//100)
answer4=a*b

print(answer1)
print(int(answer2))
print(answer3)
print(answer4)