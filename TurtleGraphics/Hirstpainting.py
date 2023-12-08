# pip install colorgram.py
import colorgram,random
import turtle as t
from turtle import Screen

tim = t.Turtle()
t.colormode(255)

# Extract color list from the image
rgb_color =[]
colors = colorgram.extract('PythonCodePractice\TurtleGraphics\image.jpg',30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color = (r,g,b)
    rgb_color.append(color)

print(rgb_color)

color_list = [(240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim.setheading(255)
tim.forward(300)
tim.setheading(0)

for _ in range(20):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


screen = Screen()
screen.exitonclick()

