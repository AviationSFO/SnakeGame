#Turtle Snake Game color and shape congigurator for 2.0.0 and newer on 8-8-2022 By Steven Weinstein


def config(script_path):
    import json
    prefs = {"highscore": 0, "bgcolor": "dark green", "foodcolor": "dark red", "foodshape": "circle", "foodnum": 2, "mutesound": True, "headcolor": "white", "tailcolor": "#13325e"}
    print('''Color Configurator
      enter a hex code or an accepted color name from this list: https://trinket.io/docs/colors NO RGB VALUES''')
    prefs["bgcolor"] = input("What color would you like the background: ")
    prefs["foodcolor"] = input("What color would you like the food: ")
    prefs["foodshape"] = input("Food shape: circle square triange or turtle: ")
    prefs["foodnum"] = input("Would you like to have 1 or 2 foods: ")
    with open(script_path.joinpath("prefs.json"), "w") as write_file:
        json.dump(prefs, write_file)
    # writing to text document
    print("Succesfuly configured!\nYou will have to restart the game for changes to take effect.")
    global changedcolor
    changedcolor = True
    return

def snakecolor(script_path):
  import json
  prefs = {"highscore": 0, "bgcolor": "dark green", "foodcolor": "dark red", "foodshape": "circle", "foodnum": 2, "mutesound": True, "headcolor": "white", "tailcolor": "#13325e"}
  print('''Color Configurator
    enter a hex code or an accepted color name from this list: https://trinket.io/docs/colors NO RGB VALUES''')
  prefs["headcolor"] = input("What color would you like the snake head: ")
  prefs["tailcolor"] = input("What color would you like the snake tail: ")
  with open(script_path.joinpath("prefs.json"), "w") as write_file:
      json.dump(prefs, write_file)
  # writing to text document
  print("Succesfuly configured!\nYou will have to restart the game for changes to take effect.")
  global changedcolor
  changedcolor = True
  return

def snakereset(script_path):
  print("\n\n\tvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv\nThere was an error in the snake color file.\nReseting the document...\n\t^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n")
  file = open(script_path.joinpath("snakeprefs.txt"), "w")
  colorhd = "white"
  colortl = "blue"
  file.write(f"{colorhd}\n{colortl}")