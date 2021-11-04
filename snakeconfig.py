#Turtle Snake congigurator for EV1.2 11-3-2021 By Steven Weinstein
import os
file = open(os.path.expanduser(
    "~/Desktop/SnakeGame/colors.txt"), "w")
print('''Color Configurator
      enter a hex code or an accepted color name from this list: https://trinket.io/docs/colors NO RGB VALUES''')
colorbg = input("What color would you like the background: ")
colorfd = input("What color would you like the food: ")
# writing to text document
file.write(colorbg+"\n"+colorfd)
print("Succesfuly configured!")