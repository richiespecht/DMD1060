# Create Title
print("Table of Powers\n")

# Get input from the user
while True:
    start = int(input("Start Number:  "))
    stop = int(input("Stop Number:  "))

    if start > stop:
        print("\nStart Number must be less than Stop Number. Please Try Again.")
        continue
    else:
        break

# Print
print("")
print("Number\tSquared\tCubed")
print("======\t=======\t=====")
for number in range(start, stop+1):
    print(number,"\t",number **2,"\t",number**3)
    

