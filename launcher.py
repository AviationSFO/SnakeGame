# Launcher for Snake Game by Steven Weintein 11-9-2021
# import required modules
import turtle
import os
import time

#screen setup
wn = turtle.Screen()
wn.setup(width = 600, height = 600)
wn.bgcolor("white")
snakegame = open(os.path.expanduser("~/Desktop/SnakeGame/turtlesnake.py"), "r")
snakegame.seek(0)
code = snakegame.read()
def launch(code):
    exec(code)
wn.onscreenclick(launch, 1, add=True)
launch(code)