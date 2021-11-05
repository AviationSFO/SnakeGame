#Turtle Snake congigurator for 1.2.2 and newer 11-4-2021 By Steven Weinstein
import os
file = open(os.path.expanduser(
    "~/Desktop/SnakeGame/colors.txt"), "w")
print('''Color Configurator
      enter a hex code or an accepted color name from this list: https://trinket.io/docs/colors NO RGB VALUES''')
colorbg = input("What color would you like the background: ")
colorfd = input("What color would you like the food: ")
shapefd = input("Food shape: circle square triange or turtle: ")
# writing to text document
file.write(colorbg+"\n"+colorfd+"\n"+shapefd)
print("Succesfuly configured!")