stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 150}
portfolio = {}

print("Enter your stock portfolio details (type 'done' when finished):")
while True:
    stock_name = input("Enter stock name (e.g., AAPL): ").upper()
    if stock_name == 'DONE':
        break
    if stock_name not in stock_prices:
        print(f"Stock '{stock_name}' not found in hardcoded prices. Please try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        portfolio[stock_name] = quantity
    except ValueError:
        print("Invalid quantity. Please enter an integer.")

total_investment = 0
print("\n--- Portfolio Summary ---")
for stock, quantity in portfolio.items():
    if stock in stock_prices:
        value = stock_prices[stock] * quantity
        total_investment += value
        print(f"{stock}: {quantity} shares * ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value: *${total_investment}*")

# Optional: Save to a text file
try:
    with open("investment_summary.txt", "w") as f:
        f.write("Stock Portfolio Summary\n\n")
        for stock, quantity in portfolio.items():
            if stock in stock_prices:
                value = stock_prices[stock] * quantity
                f.write(f"{stock}: {quantity} shares * ${stock_prices[stock]} = ${value}\n")
        f.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("Summary saved to investment_summary.txt")
except IOError as e:
    print(f"Error saving file: {e}")