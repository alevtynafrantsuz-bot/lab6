actions = {
    'FB': 10.75,
    'HPQ': 37.2,
    'ACME': 45.23,
    'IBM': 205.55,
    'AAPL': 612.78
}



for  IDaction, price in sorted(actions.items(), key=lambda pair: pair[1]):
    print(IDaction, ':', price)