# Python Snake Game by Steven Weinstein on 11-8-2021. Version available in version.txt
# import required modules
import turtle
import time
import random
import os
TK_SILENCE_DEPRECATION = 1
error = False
delay = 0.1
score = 0
highdoc = open(os.path.expanduser(
    "~/Desktop/SnakeGame/highest_score_local.txt"), "r+")
colordoc = open(os.path.expanduser(
    "~/Desktop/SnakeGame/colors.txt"), "r")
colist = colordoc.read()
colist = colist.split("\n")
temp_high_score = highdoc.read()

global high_score
try:
    high_score = int(temp_high_score)
except ValueError:
    high_score = 0
    error = True
    print("Error: highest_score_local.txt is not an integer")

# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game Project V1.2.4")
wn.bgcolor(colist[0])
# the width and height can be put as user's choice
wn.setup(width=600, height=600)
wn.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
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
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

def DEVTOOLRESET():
    head.direction = "Stop"
    head.goto(0,0)

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

segments = []


# Main Gameplay
while True:
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f"Score : {score} High Score : {high_score} ",
                  align="center", font=("candara", 24, "bold"))
    if head.distance(food) < 20:
        x = round(random.randint(-270, 270), 24)
        y = round(random.randint(-270, 270), 24)
        food.goto(x, y)

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 1
        if error == True:
            high_score = score
        else:
            if score > int(high_score):
                high_score = score
                highdoc = open(os.path.expanduser(
                    "~/Desktop/SnakeGame/highest_score_local.txt"), "w")
                highdoc.write(str(high_score))
                highdoc.close()
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
        if segment.distance(head) < 20:
            head.direction = "Up"
            head.goto(0,600)
            time.sleep(0.1)
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)

wn.mainloop()
