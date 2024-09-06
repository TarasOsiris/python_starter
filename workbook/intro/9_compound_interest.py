deposited = float(input("Enter the deposited amount: "))

INTEREST_RATE = 0.04

# Simple version - print the rows manually, more complex - loop
current_amount = deposited
for year in range(1, 4):
    current_amount += current_amount * INTEREST_RATE
    print(f"After first year {year} the sum is {current_amount:.2f}")
