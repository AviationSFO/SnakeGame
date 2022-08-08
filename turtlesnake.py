# Python Snake Game by Steven Weinstein on 8-8-2022. Version available in version.txt
# import required modules
TK_SILENCE_DEPRECATION = 1
from platform import python_version
import json
import threading as thr
import snakeconfig
from random import randint, choice
from time import sleep
import turtle
from pathlib import Path
script_path = Path(__file__, '..').resolve()
# checking if python version is compatible
pyversion = python_version()
print("Your python version is:")
print(pyversion)
if (
    "3.6" in pyversion or
    "3.7" in pyversion or
    "3.8" in pyversion or
    "3.9" in pyversion or
    "3.10" in pyversion  or
    "3.11" in pyversion
):
    print("Python version check pass")
else:
    print("v"*20)
    print("Please upgrade your python to be version 3.6 or newer, terminating process")
    print("^"*20)
    quit()
foodnum = 1
global changedcolor
changedcolor = False
# default options:
prefs = {
    "highscore": 0,
    "bgcolor": "dark green",
    "foodcolor": "navy",
    "foodshape": "square",
    "foodnum": 2,
    "mutesound": True,
    "headcolor": "white",
    "tailcolor": "blue"
}
try:
    from pygame import mixer
    noplaysound = False
    mixer.init()
except:
    noplaysound = True
global high_score
global mutesound
with open(script_path.joinpath("prefs.json"), "r") as read_file:
    prefs = json.load(read_file)
    high_score = prefs["highscore"]
    bgcolor = prefs["bgcolor"]
    foodcolor = prefs["foodcolor"]
    foodshape = prefs["foodshape"]
    foodnum = prefs["foodnum"]
    mutesound = prefs["mutesound"]
    tailcolor = prefs["tailcolor"]
    headcolor = prefs["headcolor"]
# defining important vars
error = False
delay = 0.025
movepertick = 5
score = 0
APIon = False
# opening files
datadoc = open(script_path.joinpath("data.txt"), "a")
foodnum = int(foodnum)

if foodnum == 2:
    APIdata = [None, None, None]
elif foodnum == 1:
    APIdata = [None]

try:
    high_score = int(high_score)
except ValueError:
    high_score = 0
    error = True
    print("Error: last highscore is not an integer.")

wn = turtle.Screen()
wn.title("Snake Game Project v1.14.0")
wn.bgcolor(bgcolor)
# the width and height can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
try:
    head.color(headcolor)
except:
    snakeconfig.snakereset()
    quit()
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
#colors = colist[1]
colors = foodcolor
shapes = foodshape
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

if foodnum == 2:
    food2 = turtle.Turtle()
    colors2 = foodcolor
    shapes2 = foodshape
    food2.speed(0)
    food2.shape(shapes2)
    food2.color(colors2)
    food2.penup()
    food2.goto(0, -200)

pen = turtle.Turtle()
pen.speed(0)
pen.shapesize(24)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write(f"Score: 0  High Score: {high_score}", align="center",
          font=("candara", 24, "bold"))

# assigning key directions


def goup():
    if head.direction != "down":
        head.direction = "up"


def godown():
    if head.direction != "up":
        head.direction = "down"


def goleft():
    if head.direction != "right":
        head.direction = "left"


def goright():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+movepertick)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-movepertick)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-movepertick)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+movepertick)


def DEVTOOLRESET():
    head.direction = "Stop"
    head.goto(0, 0)
    global high_score
    high_score = 0
    global prefs
    prefs = {
        "highscore": 0,
    }
    with open(script_path.joinpath("prefs.json"), "w") as write_file:
        json.dump(prefs, write_file)
    quit()


def colorconfig():
    snakeconfig.config()


def snakerecolor():
    snakeconfig.snakecolor()


def APItoggle():
    global APIon
    if APIon:
        APIon = False
    else:
        APIon = True


def APIproc():
    dist1 = head.distance(food)
    APIdata[0] = dist1
    if foodnum == 2:
        dist2 = head.distance(food2)
        print(APIdata)
        APIdata[1] = dist2
        try:
            APIdata[2] = (int(APIdata[0]) + int(APIdata[1]))/2
        except IndexError:
            APIdata.append((int(APIdata[0]) + int(APIdata[1]))/2)
        datadoc.write(
            f"({round(APIdata[0], 2)}),({round(APIdata[1], 2)}),({round(APIdata[2], 3)})\n")
    elif foodnum == 1:
        datadoc.write(f"({round(APIdata[0], 2)})\n")


def playswallow():
    if not noplaysound:
        mixer.music.load(script_path.joinpath("extrafiles/swallow.mp3"))
        mixer.music.play()


def playsmash():
    if not noplaysound:
        mixer.music.load(script_path.joinpath("extrafiles/smash.mp3"))
        mixer.music.play()


def togglemute():
    global mutesound
    if mutesound:
        mutesound = False
    else:
        mutesound = True


def config():
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
    with open(script_path.joinpath("prefs.json"), "w") as write_file:
        json.dump(prefs, write_file)
    # writing to text document
    print("Succesfuly configured!\nYou will have to restart the game for changes to take effect.")
    global changedcolor
    changedcolor = True
    return


def snakecolor():
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
    prefs["headcolor"] = input("What color would you like the snake head: ")
    prefs["tailcolor"] = input("What color would you like the snake tail: ")
    with open(script_path.joinpath("prefs.json"), "w") as write_file:
        json.dump(prefs, write_file)
    # writing to text document
    print("Succesfuly configured!\nYou will have to restart the game for changes to take effect.")
    global changedcolor
    changedcolor = True
    return


def exit():
    wn.bye()


wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")
wn.onkeypress(goup, "W")
wn.onkeypress(godown, "S")
wn.onkeypress(goleft, "A")
wn.onkeypress(goright, "D")
wn.onkeypress(goup, "Up")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")
wn.onkeypress(DEVTOOLRESET, "/")
wn.onkeypress(DEVTOOLRESET, "r")
wn.onkeypress(DEVTOOLRESET, "?")
wn.onkeypress(DEVTOOLRESET, "R")
wn.onkeypress(APItoggle, "0")
wn.onkeypress(config, "9")
wn.onkeypress(snakecolor, "8")
wn.onkeypress(togglemute, "m")
wn.onkeypress(togglemute, "M")
wn.onkeypress(exit, "Escape")
segments = []
prefs = {}

# Main Gameplay
while True:
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        if not mutesound:
            playsmash()
        sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.025
        pen.clear()
        pen.write(f"Score: {score} High Score: {high_score} ",
                  align="center", font=("candara", 24, "bold"))
    if head.distance(food) < 20:
        x = round(randint(-270, 270), 24)
        y = round(randint(-270, 270), 24)
        if mutesound == False:
            if __name__ == '__main__':
                # creating thread
                soundt = thr.Thread(target=playswallow, args=())
                soundt.start()
        food.goto(x, y)

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        try:
            new_segment.color(tailcolor)
        except:
            snakeconfig.snakereset()
            quit()
        new_segment.penup()
        segments.append(new_segment)
        score += 1
        if error == True:
            high_score = score
        else:
            if score > int(high_score):
                high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    if foodnum == 2:
        if head.distance(food2) < 20:
            x2 = round(randint(-270, 270), 24)
            y2 = round(randint(-270, 270), 24)
            if mutesound == False:
                playswallow()
            food2.goto(x2, y2)

            # Adding segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            try:
                new_segment.color(tailcolor)
            except:
                snakeconfig.snakereset()
                quit()
            new_segment.penup()
            segments.append(new_segment)
            score += 1
            if error == True:
                high_score = score
            else:
                if score > int(high_score):
                    high_score = score
            pen.clear()
            pen.write("Score: {} High Score: {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
    # Checking for head collisions with body segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < movepertick:
            if mutesound == False:
                playsmash()
            head.goto(0, 600)
            sleep(delay)
            sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            colors = choice(['red', 'blue', 'green'])
            shapes = choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments = []

            score = 0
            delay = 0.025
            pen.clear()
            pen.write(f"Score: {score} High Score: {high_score} ",
                      align="center", font=("candara", 24, "bold"))

    if APIon == True:
        if __name__ == "__main__":
            # creating thread
            t1 = thr.Thread(target=APIproc, args=())
            t1.start()

    prefs = {
        "highscore": high_score,
        "bgcolor": bgcolor,
        "foodcolor": foodcolor,
        "foodshape": foodshape,
        "foodnum": foodnum,
        "mutesound": mutesound,
        "headcolor": headcolor,
        "tailcolor": tailcolor
    }

    if changedcolor == False:
        with open(script_path.joinpath("prefs.json"), "w") as write_file:
            json.dump(prefs, write_file)
    else:
        quit()

    sleep(delay)
