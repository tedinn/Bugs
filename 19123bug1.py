def calculate_total_price(prices):
    total = 0
    for price in prices:
        total += price
    return total

# Using the function
prices = [10, 20, '30', 40, 50]  # '30' is mistakenly entered as a string
total_price = calculate_total_price(prices)
print("Total price:", total_price)
