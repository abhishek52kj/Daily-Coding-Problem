def max_profit(stock_prices):
  if len(stock_prices) < 2:
    return 0  # If there are less than two prices, no profit can be made

  min_price = stock_prices[0]
  max_profit = 0

  for price in stock_prices[1:]:
    max_profit = max(max_profit, price - min_price)
    min_price = min(min_price, price)

  return max_profit


# Example usage:
stock_prices = [9, 11, 8, 14, 5, 7, 10]
result = max_profit(stock_prices)
print(result)  # Output: 5
