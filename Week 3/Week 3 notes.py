
score = int(input("Enter test score: "))
if score >= 90:
    grade = "A"
elif score >= 80:   #elif = else if
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:               #if nothing else is true, run this
    grade = "F"
print()
print("Grade =\t " + grade)



print("Enter 'exit' when you you're done.\n")
while True:
    data = input("Enter an interget to square: ")
    if data == "exit":
        break
    i = int(data)
    print(i, "squared is", i * i, "\n")
print("Okay, bye!")



investment = 10000
x = int(input("Enter years: "))
for i in range(x):
    yearly_interest = investment * .05
    investment = investment + yearly_interest
invetment = round(investment, 2)
print(investment)



year = 0
investment = 10000
while year < 20:
    yearly_interest = investment * .05
    investment = investment + yearly_interest   # investment += yearly_interest
    year += 1
investment = round(investment, 2)
print(investment)
