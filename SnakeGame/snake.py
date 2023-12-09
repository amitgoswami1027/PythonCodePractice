from turtle import Turtle

STARTING_POS = [(0,0) , (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT =180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            x = self.segments[seg_num-1].xcor()
            y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x,y)
            
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[0].setheading(UP)

    def down(self):
        self.segments[0].setheading(DOWN)

    def right(self):
        self.segments[0].setheading(RIGHT)

    def left(self):
        self.segments[0].setheading(LEFT)
