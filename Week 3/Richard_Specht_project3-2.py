# Richard Specht Project 3-2: Tip Calculator

print("Tip Calculator \n")

#User input for the total cost of their meal
meal_cost = float(input("Cost of meal:\t"))
print()

#Creates variables for the Tip amount and Total amount for 15%
tip_fifteen = meal_cost * .15
total_fifteen = meal_cost + tip_fifteen
print("15%")
print("Tip amount:\t" + str(round(tip_fifteen, 2)))
print("Total amount:\t" + str(round(total_fifteen, 2)))
print()

#Creates variables for the Tip amount and Total amount for 20%
tip_twenty = meal_cost * .2
total_twenty = meal_cost + tip_twenty
print("20%")
print("Tip amount:\t" + str(round(tip_twenty, 2)))
print("Total amount:\t" + str(round(total_twenty, 2)))
print()

#Creates variables for the Tip amount and Total amount for 25%
tip_twentyfive = meal_cost * .25
total_twentyfive = meal_cost + tip_twentyfive
print("25%")
print("Tip amount:\t" + str(round(tip_twentyfive, 2)))
print("Total amount:\t" + str(round(total_twentyfive, 2)))





