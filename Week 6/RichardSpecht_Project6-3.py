#!/usr/bin/env python3

# Title: RichardSpecht_Project6-3.py
# Name: Richard Specht
# Date: 10/10/2023
# Description: Creates a program that a user can use to manage the primary email address and phone number for a contact

# Define functions
def display_title():
    print("Contact Manager")
    print("")

def display_menu():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view  - View a contact")
    print("add  - Add a contact")
    print("del  - Delete a contact")
    print("Exit - Exit program")
    print()
    
def list(contact_list):
    i = 1
    for row in contact_list:
        print(str(i) + ". " + row[0])
        i += 1
    print()

def view(contact_list):
    number = int(input("Number: "))
    if number < 1 or number > len(contact_list):
        print("Invalid contact number.")
    else:
        contact = contact_list[number-1]
        print("Name: " + contact[0])
        print("Email: " + contact[1])
        print("Phone: " + contact[2])
    print()

def add(contact_list):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contact_list.append(contact)
    print(contact[0] + " was added.\n")

def delete(contact_list):
    number = int(input("Number: "))
    if number < 1 or number > len(contact_list):
        print("Invalid contact number.")
    else:
        contact = contact_list.pop(number-1)
        print(contact[0] + " was deleted")
    print()
               

# Define main function 
def main():
    contact_list = [["Eric Idle", "eric@ericidle.com", "516-093-2319"],
                    ["Mike Murach", "mike@mikemurach.com", "559-123-4567"]]

    display_title()
    display_menu()

    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list(contact_list)
        elif command.lower() == "view":
            view(contact_list)
        elif command.lower() == "add":
            add(contact_list)
        elif command.lower() == "del":
            delete(contact_list)
        elif command.lower() == "exit":
            break
        else:
            print ("Invalid command. Please try again.")

    print ("Bye!")

if __name__ == "__main__":
    main()
