stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

portfolio = {}

total_value = 0

print("Stock Portfolio Tracker")

for stock in stocks:
    quantity = int(input(f"Enter quantity for {stock}: "))
    portfolio[stock] = quantity

for stock, quantity in portfolio.items():
    value = stocks[stock] * quantity
    total_value += value
    print(f"{stock}: {quantity} shares × ${stocks[stock]} = ${value}")

print("\nTotal Portfolio Value = $", total_value)

with open("portfolio_report.txt", "w") as file:
    file.write(f"Total Portfolio Value = ${total_value}\n")
    for stock, quantity in portfolio.items():
        value = stocks[stock] * quantity
        file.write(f"{stock}: {quantity} shares = ${value}\n")

print("Portfolio report saved successfully!")
