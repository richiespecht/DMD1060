# Week 7 Notes

movies = [["The Holy Grail", 1975, 9.99],
          ["Life of Brian", 1979, 12.30],
          ["The Meaning of Life", 1983, 7.50]]

movie = ["Shrek", 2001, 10.00]

movies.append(movie)
print (movies)

print (movies[1][2])

for movie in movies:
    for item in movie:
        print (item, "|")
    print ()


import random
numlist = [5, 15, 84, 3, 14, 2, 8, 10, 14, 25]

amount = numlist.count(14)       # Counts the number of time qualifier (number in perentheses) shows up in the list
print (amount)


numlist.reverse()                # Reveres the lists
print (numlist)


total = sum(numlist)             # gives you the sum of all the numbers in a list
print (total)              


numlist.sort()                   # sorts the items in the list


minimum = min(numlist)           # prints the lowest number in a list
print (minimum)


maximum = max(numlist)           # prints the highest number in a list
print (maximum)


choice = random.choice(numlist)  # picks a random number in the list
print (choice)


random.shuffle(numlist)          # shuffles the entire list randomly





foodlist = ["orange", "apple", "Pear", "banana"]
sorted_foodlist = sorted(foodlist)
print(sorted_foodlist)

sorted_foodlist = sorted(foodlist, key=str.lower)
print(sorted_foodlist)





numbers = [5, 15, 84, 3, 14]

firstthree = numbers [0:3]    # takes all the numbers in the lis UP TO the 3rd index
print (firstthree)




inventory = ["staff", "robe"]
chest = ["scroll", "pestle"]

combined = inventory + chest
print (combined)


















