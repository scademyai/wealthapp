import requests
import json

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
    return [get_stock(ticker) for ticker in s_list]

def get_stock_response(ticker):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }
    
    return requests.get(url, headers=headers)
    

def get_stock(ticker:str) -> dict:
    
    response = get_stock_response(ticker)
    
    if response.status_code != 200:
        return None
    else:
        data = response.json()
        if not (latest_price := data["chart"]["result"][0]["meta"].get("regularMarketPrice")):
            return None
        
        return {
            "ticker": ticker,
            "price": latest_price
        }

def get_a_single_stock(stockTicker:str):
    return next(filter(lambda stock: stock["ticker"] == stockTicker, STOCKS))
