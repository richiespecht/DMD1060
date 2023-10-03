
# Defining a funtion and calling it 'bing'
def bing():
   print("bing bing bing")
   print("Inside the function")
    
bing()      # Calling for the function 'bing' to run
print("Outside the function")

#--------------------------------------

#creating a function with 2 arguments
def add_num(num1, num2):
    sum = num1 + num2
    print(sum)

add_num(4,5)

#--------------------------------------

#return the answer to a variable
def add_num(num1, num2):
    sum = num1 + num2
    return sum      # must have or nothing will run

result = add_num(4,5)
print(result)

#--------------------------------------

def get_square(num):
    return num*num

for i in [1,2,3]:
    result = get_square(i)
    print("Sqaure of", i, "=", result)

#--------------------------------------

# any variable created inside a funtion is only applicable inside that function (called Local)
def greet():
    message = "Hello"
    print("Local Variable:", message)

greet()
#print(message) wouldn't work because 'message' was defined inside the function

#--------------------------------------

message = "Hello"   # calleda Global variable because it was created outside a function
def greet():
    message = "Hello"
    print("Local Variable:", message)

greet()
print(message)

#--------------------------------------

message = "Hello"
def greet():
    var = "Goodbye"
    print("Local Variable:", var)
    return var

message = greet()
print(message)

#--------------------------------------

c = 1
def add():
    global c  #dont create a new 'c', go use the global one outside the function
    c += 2
    print(c)

add()

#--------------------------------------

