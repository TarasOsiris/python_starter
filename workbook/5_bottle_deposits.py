CASH_PER_SMALL = 0.10
CASH_PER_LARGE = 0.25

while True:
    less_than_litre_containers = int(input("how many smaller than litre? "))
    more_than_litre_containers = int(input("how many larger than litre? "))

    total = less_than_litre_containers * CASH_PER_SMALL + more_than_litre_containers * CASH_PER_LARGE

    # A few ways to achieve the same thing
    print("Total refund will be $%.2f" % total)  # old formatting
    print(f"Total is ${total:.2f}")
    print("Total:", "${:.2f}".format(total))
