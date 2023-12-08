
import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

#tim.speed("fastest")
#tim.color(random_color())
#tim.circle(100)

#current_heading = tim.heading()
#tim.setheading(current_heading + 18)
#tim.circle(100)

tim.speed("fastest")

def create_spiralgraph(size_of_graph):

    for _ in range(int(360/size_of_graph)):
        tim.color(random_color())
        #tim.circle(100)

        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_graph)
        tim.circle(100)

create_spiralgraph(5)











screen = Screen()
screen.exitonclick()