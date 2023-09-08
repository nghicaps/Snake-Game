from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.reset()

    def create_snake(self):
        for i in range(3):
            self.add_segment((-i * 20 + 20, 0))

    def add_segment(self, index):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(index)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_index - 1].xcor()
            new_y = self.segments[seg_index - 1].ycor()
            self.segments[seg_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(400, 400)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
