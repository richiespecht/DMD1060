first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
birth_year = input("Enter Birth Year: ")
temp_password = first_name + "*" + str(birth_year)
full_name = first_name + " " + last_name

print("")
print ("Registration Form")
print("")
print("First Name:\t" + first_name)
print("Last Name:\t" + last_name)
print("Birth Year:\t" + str(birth_year))
print("")
print("Welcome " + full_name + "!")
print("Your registration is complete.")
print("Your temporary password is: " + temp_password)
      


      
