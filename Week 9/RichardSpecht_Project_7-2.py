#!/usr/bin/env python3

# Title: RichardSpecht_Project7-2.py
# Name: Richard Specht
# Date: 10/24/2023
# Description: Create a program that keeps track of the items that a wizard is carrying. 

# Import modules
import random
import copy

wizard_all_items = "wizard_all_items.txt"
wizard_inventory = "wizard_inventory.txt"

# Define functions
def read_items():
    items = []
    with open (wizard_all_items) as file:
        for line in file:
            line = line.replace("\n", "")
            items.append(line)
        return items

def read_inventory():
    inventory = []
    with open (wizard_inventory) as file:
            for line in file:
                line = line.replace("\n", "")
                inventory.append(line)
            return inventory
    
def write_inventory(inventory):
    with open(wizard_inventory, "w") as file:
        for item in inventory:
            file.write(item + "\n")

def display_title():
    print("The Wizard Inventory program")
    print("")

def display_menu():
    print("COMMAND MENU")
    print("walk - Walk down the path")
    print("show - Show all items")
    print("drop  - Drop an item")
    print("exit - Exit program")
    print()

def walk(inventory):
    items = read_items()
    item = random.choice(items)
    print ("While walking down a path, you see a " + item)
    choice = input("Do you want to grab it? (y/n): ")
    if choice.lower() == "y":
        if len(inventory) >= 4:
            print ("You can't carry any more items. Drop something first.")
        else:
            inventory.append(item)
            print ("You picked up a " + item + "\n")
            write_inventory(inventory)
                        

def show(inventory):
    for number, item in enumerate(inventory, start=1):
        print(f"{number}. {item}")
    print()

def drop(inventory):
    number = int(input("Number: "))
    if number < 1 or number > len(inventory):
        print("Invalid item number.\n")
    else:
        item = inventory.pop(number-1)
        print(item + " was dropped.\n")


# Define main function 
def main():
    display_title()
    display_menu()
    
    inventory = read_inventory() 
    
    while True:
        command = input("Command: ")
        if command.lower() == "walk":
            walk(inventory)
        elif command.lower() == "show":
            show(inventory)
        elif command.lower() == "drop":
            drop(inventory)
        elif command.lower() == "exit":
            break
        else:
            print ("Invalid command. Please try again.")

    print ("Bye!")
    write_inventory(inventory)         

if __name__ == "__main__":
    main()
