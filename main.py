
from turtle import Turtle, Screen
import time
from random import choice

HEADING = 0
CYCLE_COMPLETED = True
current_positions = [(0, 0), (-20, 0), (-40, 0)]


def direction(heading):

    global CYCLE_COMPLETED
    global HEADING
    if HEADING == 0 and heading == 180:
        return
    elif HEADING == 90 and heading == 270:
        return
    elif HEADING == 180 and heading == 0:
        return
    elif HEADING == 270 and heading == 90:
        return
    else:
        HEADING = heading
    CYCLE_COMPLETED = False
    return


def north():
    global CYCLE_COMPLETED
    if CYCLE_COMPLETED:
        heading = 90
        direction(heading)


def east():
    global CYCLE_COMPLETED
    if CYCLE_COMPLETED:
        heading = 0
        direction(heading)


def south():
    global CYCLE_COMPLETED
    if CYCLE_COMPLETED:
        heading = 270
        direction(heading)


def west():
    global CYCLE_COMPLETED
    if CYCLE_COMPLETED:
        heading = 180
        direction(heading)


def move_snek(snek, food):
    global CYCLE_COMPLETED
    global HEADING
    global current_positions

    append_new_segment = False

    current_positions = []
    for segment in snek:
        current_x = segment.xcor()
        current_y = segment.ycor()
        current_positions.append((current_x, current_y))

    print(current_positions)
    move_to_x = current_positions[0][0]
    move_to_y = current_positions[0][1]
    snek[0].setheading(HEADING)

    if HEADING is 0:
        snek[0].goto(x=move_to_x + 20, y=move_to_y)
    elif HEADING is 90:
        snek[0].goto(x=move_to_x, y=move_to_y + 20)
    elif HEADING is 180:
        snek[0].goto(x=move_to_x - 20, y=move_to_y)
    else:
        snek[0].goto(x=move_to_x, y=move_to_y - 20)

    if (snek[0].xcor(), snek[0].ycor()) in current_positions:
        return False
    if snek[0].xcor() > 290 or snek[0].xcor() < -290:
        return False

    if snek[0].ycor() > 290 or snek[0].ycor() < -290:
        return False

    if snek[0].xcor() == food.xcor() and snek[0].ycor() == food.ycor():
        place_food(food)
        new_segment_co_ords = (snek[-1].xcor(), snek[-1].ycor())
        append_new_segment = True



    for i in range(1, len(snek)):
        move_from_x = current_positions[i][0]
        move_from_y = current_positions[i][1]
        co_ord = (move_to_x, move_to_y)
        snek[i].goto(co_ord)
        move_to_x = move_from_x
        move_to_y = move_from_y


    if append_new_segment:
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(new_segment_co_ords)
        snek.append(new_segment)

    screen.update()
    CYCLE_COMPLETED = True
    return True


def place_food(food):
    global current_positions
    positions = [-180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180]
    choosing_co_ordinates = True
    while choosing_co_ordinates:
        random_x = choice(positions)
        random_y = choice(positions)
        co_ordinates = (random_x, random_y)

        if co_ordinates not in current_positions:
            food.hideturtle()
            food.goto(co_ordinates)
            food.showturtle()
            return



screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snek")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkey(north, key="w")
screen.onkey(east, key="d")
screen.onkey(south, key="s")
screen.onkey(west, key="a")


starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snek = []

for position in current_positions:
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    snek.append(new_segment)

food = Turtle(shape="circle")
food.penup()
food.color("white")

place_food(food)
screen.update()

game_is_on = True
while game_is_on:
    game_is_on = move_snek(snek, food)
    time.sleep(0.1)


screen.exitonclick()
