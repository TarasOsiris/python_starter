meal_cost = float(input("Enter meal cost: "))

TAX_RATE_PERCENT = 0.07
TIP_PERCENT = 0.18

tax = meal_cost * TAX_RATE_PERCENT
tip = meal_cost * TIP_PERCENT
total = meal_cost + tax + tip

print(f"tax: ${tax:.2f}", f"tip: ${tip:.2f}", f"total: ${total:.2f}")
