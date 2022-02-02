#Turtle Snake Game color and shape congigurator for 1.8.0 and newer 2-2-2021 By Steven Weinstein
def config():
    import os
    file = open(os.path.expanduser(
        "~/Desktop/SnakeGame/prefs.txt"), "w")
    print('''Color Configurator
      enter a hex code or an accepted color name from this list: https://trinket.io/docs/colors NO RGB VALUES''')
    colorbg = input("What color would you like the background: ")
    colorfd = input("What color would you like the food: ")
    shapefd = input("Food shape: circle square triange or turtle: ")
    fdnum = input("Would you like to have 1 or 2 foods: ")
    # writing to text document
    file.write(f"{colorbg}\n{colorfd}\n{shapefd}\n{fdnum}")
    print("Succesfuly configured!\nYou will have to restart the game for changes to take effect.")

def snakecolor():
  import os
  file = open(os.path.expanduser(
        "~/Desktop/SnakeGame/snakeprefs.txt"), "w")
  print('''Color Configurator
      enter a hex code or an accepted color name from this list: https://trinket.io/docs/colors NO RGB VALUES''')
  colorhd = input("What color would you like the snake head to be: ")
  colortl = input("Enter the color you would like the tail color to be: ")
  file.write(f"{colorhd}\n{colortl}")
  print("Succesfuly configured!\nYou will have to restart the game for changes to take effect.")