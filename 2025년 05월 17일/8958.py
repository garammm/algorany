n = int(input())

for _ in range(n):
    line = input()
    count = 0
    streak = 0

    for c in line:
        if c == 'O':
            streak+=1
            count +=streak
        else:
            streak = 0

    print(count)