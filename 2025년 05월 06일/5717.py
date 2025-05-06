# M = int(input())
# F = int(input())


# friend = M+F
# print(friend)

while 1:
    M, F = map(int, input().split())
    if M == 0 and F == 0:
        break
    print(M + F)
