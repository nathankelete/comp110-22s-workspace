"""EX04 - Turtle Scene.

Random selection for drawings is implemented in the sunny_or_cloudy list.
"""

__author__ = "730484959"

from turtle import Turtle, colormode, done
from random import randint
colormode(255)


def reposition(turtle: Turtle, x: float, y: float) -> None:
    """Repositions the shape to the given x and y values."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0.0)
    turtle.pendown()


def triangle(turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a triangle of the given width whose top-left corner is located at x, y."""
    reposition(turtle, x, y)
    i: int = 0
    while (i < 3):
        turtle.forward(width)
        turtle.left(120)
        i += 1
    

def rectangle(turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a rectangle of the given width whose top-left corner is located at x, y."""
    reposition(turtle, x, y)
    i: int = 0
    while i < 4:
        turtle.forward(width)
        turtle.left(90)
        i += 1
    

def square(turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    reposition(turtle, x, y)
    i: int = 0
    while i < 4:
        turtle.forward(width)
        turtle.right(90)
        i = i + 1
    

def circle(turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a circle of the given radius whose top-left corner is located at x, y."""
    turtle.fillcolor(255, 165, 0)
    turtle.begin_fill()
    reposition(turtle, x, y)
    turtle.circle(radius)
    turtle.end_fill()
    done()


def cloud(turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draws a cloud with circles of the given radius whose top-left corner is located at x, y."""
    reposition(turtle, x, y)
    i: int = 0
    while i < 7:
        turtle.circle(radius)
        turtle.right(90)
        turtle.left(32)
        i += 1


def main() -> None:
    """The entrypoint of my scene."""
    house: Turtle = Turtle()
    house.color("red")
    square(house, -5, 5, 100)
    house.color("green")
    triangle(house, -5, 5, 100)
    house.color("brown")
    rectangle(house, 30, -95, 25)
    house.color("black")
    square(house, 2, -2, 30)
    square(house, 50, -2, 30)
    sunny_or_cloudy: list[int] = list()
    sunny_or_cloudy.append(randint(1, 2))
    if sunny_or_cloudy[len(sunny_or_cloudy) - 1] == 1:
        """If the list randomly selects the integer 1, it will be sunny."""
        circle(house, 200, 125, 75)
    else: 
        """If the list randomly selects 2, it will be cloudy."""
        cloud(house, 200, 125, 30)
        
    
if __name__ == "__main__":
    main()
