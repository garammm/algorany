coin, money = map(int,input().split())
coins = [int(input()) for _ in range(coin)]
coins.sort(reverse=True)

coin_counting =0

for coin in coins:
    if money ==0:
        break
    count = money //coin
    coin_counting += count
    money -= count * coin


print(coin_counting)

