#Richard Specht Project 3-1: Letter Grade Converter


print("Letter Grade Converter")

choice = "y"
while choice.lower() == "y":
    print()                                         
    score = int(input("Enter numerical grade: "))
    if score >= 88:
        grade = "A"
    elif score >= 80 and score <= 87:   
        grade = "B"
    elif score >= 67 and score <= 79:
        grade = "C"
    elif score >= 60 and score <= 66:
        grade = "D"
    else:               
        grade = "F"
    print("Letter Grade: " + grade)
    print ()
    choice = input("Continue? (y/n): ")

 
print()
print("Bye!")

    
    
