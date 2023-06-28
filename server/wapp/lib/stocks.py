STOCKS = [
    {
        "ticker": "TSLA",
        "price": "270.00",
        "volume": "1000000"
    },
    {
        "ticker": "AAPL",
        "price": "200.00",
        "volume": "2000000"
    },
    {
        "ticker": "GOOG",
        "price": "1000.00",
        "volume": "3000000"
    }
]

def get_stocks(s_list):
    if len(s_list) == 1:
        return next(filter(lambda stock: stock["ticker"] == s_list[0], STOCKS))
    else:
        return [stock for stock in STOCKS if stock["ticker"] in s_list]
def get_a_single_stock(stockTicker:str):
    return next(filter(lambda stock: stock["ticker"] == stockTicker, STOCKS))