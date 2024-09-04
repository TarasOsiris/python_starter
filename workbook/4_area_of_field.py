length: float = float(input("Enter the length of the field (in feet): "))
width: float = float(input("Enter the width of the field (in feet): "))

SQFT_PER_ACRE = 43560
area = length * width / SQFT_PER_ACRE

print("The area of the field is", area, "acres")
