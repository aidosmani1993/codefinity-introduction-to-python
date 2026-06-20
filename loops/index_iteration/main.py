prices = [29.99, 45.50, 12.75, 38.20]

discount_rate = [0.10, 0.20, 0.15, 0.05]
for i in range(len(prices)):
    new_price = prices[i] * (1 - discount_rate[i])
    prices[i] = new_price
    print(f"Updated price fot item {i}: ${prices[i]:.2f}")