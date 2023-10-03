#!/usr/bin/env python3

# Title: RichardSpecht_Project4-2.py
# Name: Richard Specht
# Date: 09/26/2023
# Description: Converts miles to feet

# Prints the title
def print_title():
    print("Hike Calculator\n")

#Converts the miles to feet
def convert_to_feet(miles):
    feet=miles*5280
    return feet

# Define main function 
def main():
    print_title()
    #Define a variable and get input from user as a float
    miles = float(input("How many miles did you walk?: "))

    #run the convert miles functions and return the feet to a variable
    feet = int(convert_to_feet(miles))
    
    #print the number of feet walked
    print("You walked", feet, "feet.")
    
if __name__ == "__main__":
    main()




