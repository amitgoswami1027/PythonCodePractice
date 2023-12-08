from turtle import Screen,Turtle

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

#segment_1 = Turtle("square")
#segment_1.color("white")

#segment_2 = Turtle("square")
#segment_2.color("white")
#segment_2.goto(-20,0)

#segment_3 = Turtle("square")
#segment_3.color("white")
#segment_3.goto(-40,0)

# Step-01 Create the snake color
starting_posiion = [(0,0) , (-20,0), (-40,0)]

for position in starting_posiion:
    segment = Turtle("square")
    segment.color("white")
    segment.goto(position)

# Step-02 : Move the snake









screen.exitonclick()




