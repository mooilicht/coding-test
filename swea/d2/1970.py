for i in range(1, int(input()) + 1):
    prices = {50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0}
    money = int(input())
    print(f"#{i}")
    for price in prices:
        prices[price] = money // price
        money = money % price
        print(prices[price], end=" ")
    print()
