MOVE_DISTANT = 20
POSITION = [(0, 0), (-20, 0), (-40, 0)]

from turtle import Turtle, Screen


class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.move_distance = 20
        self.head = self.segments[0]

    def create_snake(self):
        for n in POSITION:
            self.add_segment(n)

    def add_segment(self, n):
        new_segments = Turtle("square")
        new_segments.color("white")
        new_segments.pu()
        new_segments.goto(n)
        self.segments.append(new_segments)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(self.move_distance)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def restart(self):
        for seg in self.segments:
            seg.goto(500, 500)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

