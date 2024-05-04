#Task 1
stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0)
]
import statistics

def avg_closing_price(stock_data):
    stock = input("Enter stock you want to analyze: ").lower()
    start_date = input("Enter start date (yyyy-mm-dd): ")
    end_date = input("Enter end date (yyyy-mm-dd): ")
    stock_info = []
    stock_in_period = []
    closing_prices = []
    for info in stock_data:
        name, date, price = info
        if stock == name.lower():
            stock_info.append(info)
        else:
            pass

    for analyzed_stock in stock_info:
        if start_date <= analyzed_stock[1] <= end_date:
            stock_in_period.append(analyzed_stock)
        else:
            pass

    for value in stock_in_period:
        closing_prices.append(value[2])
    
    avg_price = statistics.mean(closing_prices)

    print(avg_price)

    

avg_closing_price(stock_data)