'''Bill'''

price = int(input())

price_1 = (price / 100) * 10
price_2 = max(min(price_1, 1000), 50)
price_3 = price +price_2
price_4 = (price_3 / 100) * 7
price_5 = price + price_4 + price_2
print(f'{price_5:.2f}')
