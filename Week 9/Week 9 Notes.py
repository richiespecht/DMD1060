outfile = open("test.txt", "w")     # overwrites then enitre file
outfile.write("Test, ")
outfile.close

outfile = open("test.txt", "a")     # adds to the end of the line
outfile.write("Richie\n")
outfile.close

with open("test.txt", "a") as outfile:
    outfile.write("Test\n")

with open("test.txt") as file:      # reads each line indidually
    for line in file:
        print (line, end="")
    print()

with open("test.txt") as file:      # reads the entire file
    contents = file.read()
    print(contents)

with open("test.txt") as file:      # read it in as a list
    members = file.readlines()
    print (members)
    print (members[0], end="")
    print (members[1])

with open("test.txt") as file:      
    member1 = file.readline()
    print (member1, end="")
    member2 = file.readline()
    print (member2)

members = ["John Cleese", "Eric Idle"]
with open("test.txt", "a") as file:
    for m in members:
        file.write(m + "\n")

members = []
with open("test.txt", "a") as file:
    for line in file:
        line = line.replace("\n", "")   # searches for "\n" and replace with ""
        members.append(line)
print(members)
