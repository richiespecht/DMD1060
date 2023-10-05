#!/usr/bin/env python3

# Title: RichardSpecht_Project6-2.py
# Name: Richard Specht
# Date: 10/05/2023
# Description: Creates a program that keeps track of the items that a wizard can carry. 

# Define functions
def display_title():
    print("The Wizard Inventory program")
    print("")

def display_menu():
    print("COMMAND MENU")
    print("Show - Show all items")
    print("Grab  - Grab an item")
    print("Edit  - Edit an item")
    print("Drop  - Drop an item")
    print("Exit - Exit program")
    print()
    
def show(item_list):
    i = 1
    for item in item_list:
        print(str(i) + ". " + item)
        i += 1
    print()

def grab(item_list):
    if len(item_list) >= 4:
        print("You can't carry any more items. Drop something first.\n")
    else:
        name = (input("Name: "))
        item_list.append(name)
        print(name + " was added.\n")
    
def edit(item_list):
    number = int(input("Number: "))
    if number < 1 or number > len(item_list):
        print("Invalid item number.")
    else:
        update = input("Updated Name: ")
        item_list[number-1] = update
        print("Item number", number, " was updated.\n")

def drop(item_list):
    number = int(input("Number: "))
    if number < 1 or number > len(item_list):
        print("Invalid item number.")
    else:
        item = item_list.pop(number-1)
        print(item + " was dropped.\n")


# Define main function 
def main():
    item_list = ["wooden staff",
                 "wizard hat",
                 "clothe shoes"]

    display_title()
    display_menu()

    while True:
        command = input("Command: ")
        if command.lower() == "show":
            show(item_list)
        elif command.lower() == "grab":
            grab(item_list)
        elif command.lower() == "edit":
            edit(item_list)
        elif command.lower() == "drop":
            drop(item_list)
        elif command.lower() == "exit":
            break
        else:
            print ("Invalid command. Please try again.")

    print ("Bye!")
       
            

if __name__ == "__main__":
    main()
