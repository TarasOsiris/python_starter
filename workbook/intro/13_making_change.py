cents = int(input("Enter the number of cents: "))

CENTS_PER_PENNY = 1
CENTS_PER_NICKEL = 5
CENTS_PER_DIME = 10
CENTS_PER_QUARTER = 25
CENTS_PER_LOONIE = 100
CENTS_PER_TOONIE = 200

print(" ", cents // CENTS_PER_TOONIE, "toonies")
cents = cents % CENTS_PER_TOONIE

print(" ", cents // CENTS_PER_LOONIE, "loonies")
cents = cents % CENTS_PER_LOONIE
