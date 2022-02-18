from turtle import Screen, Turtle
import time

#create a new screen
screen = Screen()

#setup screen
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_postions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

#put snake body on screen
for position in starting_postions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) -1, 0, -1): #(start=2, end=0, step=-1)
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)


    segments[0].forward(20)










screen.exitonclick()
