# Create Title
print("Change Calculator")

choice = "y"
while choice.lower() == "y":

    # Get input from the user
    cents = int(input("\nEnter number of cents (0-99): "))

    # Calculate number of quaters
    quarters = cents // 25
    cents = cents % 25

    # Calculate number of dimes
    dimes = cents // 10
    cents = cents % 10

    # Calculate number of nickles and pennies
    nickles = cents // 5
    cents = cents % 5
    pennies = cents

    # Display the breakdown of change
    print()
    print("Quarters: ", quarters)
    print("Dimes:    ", dimes)
    print("Nickles:  ", nickles)
    print("Pennies:  ", pennies)

    # Ask user if they want to continue
    choice = input("\nContinue? (y/n): ")
print("\nBye!")
