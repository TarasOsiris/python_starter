efficiency_mpg = float(input("Enter fuel efficiency in MPG: "))  # miles per gallon

KM_PER_MILE = 1.60934
LITRE_PER_GALLON = 3.78541
# See https://www.mpgtolitres.com/ for the explanation
efficiency_l_per_km = 100 / (efficiency_mpg * KM_PER_MILE / LITRE_PER_GALLON)  # km per litre

print(f"fuel efficiency is {efficiency_l_per_km:.2f} L/100km")
