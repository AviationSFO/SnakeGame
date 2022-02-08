#Turtle Snake Game color and shape congigurator for 1.10.1 and newer on 2-8-2022 By Steven Weinstein
def config():
    import os
    import json
    prefs = {
    "highscore": 0,
    "bgcolor": "dark green",
    "foodcolor": "navy",
    "foodshape": "square",
    "foodnum": 2,
    "mutesound": True
}
    print('''Color Configurator
      enter a hex code or an accepted color name from this list: https://trinket.io/docs/colors NO RGB VALUES''')
    prefs["bgcolor"] = input("What color would you like the background: ")
    prefs["foodcolor"] = input("What color would you like the food: ")
    prefs["foodshape"] = input("Food shape: circle square triange or turtle: ")
    prefs["foodnum"] = input("Would you like to have 1 or 2 foods: ")
    with open(os.path.expanduser(
        "~/Desktop/SnakeGame/prefs.json"), "w") as write_file:
        json.dump(prefs, write_file)
    # writing to text document
    # file.write(f"{colorbg}\n{colorfd}\n{shapefd}\n{fdnum}")
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

def snakereset():
  import os
  print("\n\n\tvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv\nThere was an error in the snake color file.\nReseting the document...\n\t^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n")
  file = open(os.path.expanduser(
        "~/Desktop/SnakeGame/snakeprefs.txt"), "w")
  colorhd = "white"
  colortl = "blue"
  file.write(f"{colorhd}\n{colortl}")