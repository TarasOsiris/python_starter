feet = float(input("Enter your height in feet: "))
inches = float(input("Enter your height in inches: "))

IN_PER_FT = 12
CM_PER_IN = 2.54

print(f"Your height is {(feet * IN_PER_FT + inches) * CM_PER_IN} cm")
