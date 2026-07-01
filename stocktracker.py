stock_prices = {"AAPL": 180,"TSLA": 250,"GOOG": 150,"MSFT": 400}
total_investment = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input(f"Enter stock {i + 1} name (AAPL, TSLA, GOOG, MSFT): ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        investment = stock_prices[stock] * quantity
        total_investment += investment
        print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}")

    else:
        print("Stock not found!")

print("\nTotal Investment Value = $", total_investment)

with open("investment.txt", "w") as file:
    file.write(f"Total Investment Value = ${total_investment}")

print("Result saved in investment.txt")