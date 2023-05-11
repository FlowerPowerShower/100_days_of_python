from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        x_cor = 0
        for snake in range(3):
            t = Turtle()
            t.shape("square")
            t.color("white")
            t.penup()
            t.setposition(x_cor, 0)
            x_cor -= 20
            self.segments.append(t)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor
            y = self.segments[seg_num - 2].ycor
            self.segments[seg_num].goto(x, y)
        self.segments[0].forward(20)
