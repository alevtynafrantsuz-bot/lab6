stocks = {
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.2,
    'JPM': 292.11,
    'XOM': 118.45
}

tech_ids = {'AAPL', 'IBM', 'HPQ'}

tech_stocks = {
    ticker: price
    for ticker, price in stocks.items()
    if ticker in tech_ids
}

for ticker, price in tech_stocks.items():
    print(ticker, price)