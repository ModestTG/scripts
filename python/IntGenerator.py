# Int Generator
# Create a string of ints with one whitespace in between. Use to create multiple
# variables with sublime
from os.path import expanduser

home = expanduser("~") + "\\Desktop"  # <-- Windows users only have Desktop

rangeStart = input("Enter starting int: ")
rangeEnd = input("Enter ending int: ")
rangeInc = input("Enter increment value: ")

intString = ""
print("Working")
for x in range(int(rangeStart), int(rangeEnd) + 1, int(rangeInc)):
	intString += str(x)
	intString += " "
intFile = open(home + "\\IntGen.txt", "w+")
intFile.write(intString)
intFile.close()

print("Complete. File saved in " + home)
