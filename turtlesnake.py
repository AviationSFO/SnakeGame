# Python Snake Game by Steven Weinstein on 2-3-2022. Version available in version.txt
# import required modules
import turtle
import time
import random
import os
import time
import snakeconfig
import threading as thr
try:
    from playsound import playsound
    noplaysound = False
except:
    noplaysound = True
# defining important vars
TK_SILENCE_DEPRECATION = 1
foodnum = 1
error = False
delay = 0.025
movepertick = 5
score = 0
APIon = False
global mutesound
# opening files
datadoc = open(os.path.expanduser(
    "~/Desktop/SnakeGame/data.txt"), "a")
highdoc = open(os.path.expanduser(
    "~/Desktop/SnakeGame/highest_score_local.txt"), "r+")
colordoc = open(os.path.expanduser(
    "~/Desktop/SnakeGame/prefs.txt"), "r")
snakedoc = open(os.path.expanduser(
    "~/Desktop/SnakeGame/snakeprefs.txt"), "r")
colist = colordoc.read()
colist = colist.split("\n")
if colist[3] == "2":
    foodnum = 2
if colist[4] == "mute:true":
    mutesound = True
else:
    mutesound = False

if foodnum == 2:
    APIdata = [None, None, None]
elif foodnum == 1:
    APIdata = [None]
temp_high_score = highdoc.read()

global high_score
high_score = 0
try:
    high_score = int(temp_high_score)
except ValueError:
    high_score = 0
    error = True
    print("Error: highest_score_local.txt is not an integer")

snakeprefs = snakedoc.read()
snakeprefs = snakeprefs.split("\n")
headcolor = snakeprefs[0]
tailcolor = snakeprefs[1]
# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game Project V1.9.0")
wn.bgcolor(colist[0])
# the width and height can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
#head.color("white")
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
colors = colist[1]
shapes = colist[2]
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

if foodnum == 2:
    food2 = turtle.Turtle()
    colors2 = colist[1]
    shapes2 = colist[2]
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
pen.write(f"Score : 0  High Score : {high_score}", align="center",
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
    head.goto(0,0)

def colorconfig():
    snakeconfig.config()

def snakerecolor():
    snakeconfig.snakecolor()

def APIactivate():
    global APIon
    APIon = True


def APIproc():
    dist1 = head.distance(food)
    if foodnum == 2:
        dist2 = head.distance(food2)
    APIdata[0] = dist1
    if foodnum == 2:
        print(APIdata)
        APIdata[1] = dist2
        try:
            APIdata[2] = (int(APIdata[0]) + int(APIdata[1]))/2
        except IndexError:
            APIdata.append((int(APIdata[0]) + int(APIdata[1]))/2)
    if foodnum == 2:
        datadoc.write(f"({round(APIdata[0], 2)}),({round(APIdata[1], 2)}),({round(APIdata[2], 3)})\n")
    elif foodnum == 1:
        datadoc.write(f"({round(APIdata[0], 2)})\n")

def playswallow():
    if noplaysound == False:
        playsound("Desktop/SnakeGame/extrafiles/swallow.mp3")

def togglemute():
    if colist[4] == "mute:true":
        colist[4] == "mute:false"
        global mutesound
        mutesound = False
    if colist[4] == "mute:false":
        colist[4] == "mute:true"
        mutesound = True
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
wn.onkeypress(DEVTOOLRESET, "?")
wn.onkeypress(DEVTOOLRESET, "r")
wn.onkeypress(DEVTOOLRESET, "R")
wn.onkeypress(APIactivate, "0")
wn.onkeypress(colorconfig, "9")
wn.onkeypress(snakerecolor, "8")
wn.onkeypress(togglemute, "m" or "M")

segments = []


# Main Gameplay
while True:
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.025
        pen.clear()
        pen.write(f"Score : {score} High Score : {high_score} ",
                  align="center", font=("candara", 24, "bold"))
    if head.distance(food) < 20:
        x = round(random.randint(-270, 270), 24)
        y = round(random.randint(-270, 270), 24)
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
                highdoc = open(os.path.expanduser(
                    "~/Desktop/SnakeGame/highest_score_local.txt"), "w+")
                highdoc.write(str(high_score))
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    if foodnum == 2:
        if head.distance(food2) < 20:
            x2 = round(random.randint(-270, 270), 24)
            y2 = round(random.randint(-270, 270), 24)
            if mutesound == False:
                if __name__ == '__main__':
                    # creating thread
                    soundt = thr.Thread(target=playswallow, args=())
                    soundt.start()
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
                    highdoc = open(os.path.expanduser(
                        "~/Desktop/SnakeGame/highest_score_local.txt"), "w+")
                highdoc.write(str(high_score))
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
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
            head.direction = "Up"
            head.goto(0,600)
            time.sleep(delay)
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments = []

            score = 0
            delay = 0.025
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))

    if APIon == True:
        if __name__ == "__main__":
            # creating thread
            t1 = thr.Thread(target=APIproc, args=())
            t1.start()
    time.sleep(delay)

# I honeslty have no idea what this line does or why I added it but it seems to break the program if I remove it, so it is here to stay.
wn.mainloop()
