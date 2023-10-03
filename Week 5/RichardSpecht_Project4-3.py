#!/usr/bin/env python3

# Title: Start_Template.py - starter template for python scripts
# Name: Richard Specht
# Date: 09/27/2023
# Description: Feet and Meters Converter


# Define functions
def display_title():
    print("Feet and Meters Converter\n")

def display_menu():
    print("Conversion Menu:")
    print("a. Feet to Meters")
    print("b. Meters to Feet")

def convert():
    option = input("Select a conversion (a/b): ")
    if option == "a":
        feet = int(input("\nEnter feet: "))
        feet = feet * 0.3048
        feet = round(feet, 2)
        print(feet, "meters")
    elif option == "b":
        meters = int(input("\nEnter meters: "))
        meters = meters / 0.3048
        meters = round(meters, 2)
        print(meters, "feet")
            

# Define main function 
def main():
    display_title()
    display_menu()
    again = "y"
    while again.lower() == "y":
        convert()
        print()
        again = input("Would you like to perform another conversion? (y/n): ")
        print()
    print("Thanks, bye!")

if __name__ == "__main__":
    main()




