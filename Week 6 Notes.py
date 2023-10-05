# Lists: basically variables with multiple items inside

num_list = [1, 2, 3, 4]
str_list = ["Mike", "Frog", "Ted", "Cat"]
mixed_list = [1, "Frog", 2.11, ""]
empty_list = []

foo = [1] * 5    # Create a list with a value of 1, and repeat it 5 times

print (foo)
print (num_list[0])     # Print the varible in the '0' index

boo = str_list[2]       # Set a specific index to a variable
print (boo)

str_list[2] = "Monkey"  # Changing a specific item in a list
print (str_list)

str_list.append("Monkey")     # puts an item at the end of a list
str_list.insert(0, "Monkey")  # inserts a item to the index called for
str_list.remove("Mike")       # removes an item from the list
str_list.pop()                # 
boo = str_list.index("Mike")  # gives the index number of a specific item
print (len(str_length))       # tells you the length of a list


