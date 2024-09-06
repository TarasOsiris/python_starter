import sys

human_years = int(input("Enter the number of human years: "))

HUMAN_TO_DOG_BEFORE_TWO = 10.5
HUMAN_TO_DOG_AFTER_TWO = 4

if human_years < 0:
    print("Please enter a positive integer")
    sys.exit()

if human_years <= 2:
    dog_years = human_years * HUMAN_TO_DOG_BEFORE_TWO
else:
    dog_years = 2 * HUMAN_TO_DOG_BEFORE_TWO + (human_years - 2) * HUMAN_TO_DOG_AFTER_TWO

print("Dog years: ", dog_years)
