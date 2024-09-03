from turtle import Turtle
pos = [(0, 0), (-10, 0), (-20, 0)]
move_dis = 20
down = 270
up = 90
right = 0
left = 180
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in pos:
            self.add_seg(position)


    def add_seg(self, position):
        turt = Turtle()
        turt.shape("square")
        turt.color("white")
        turt.pu()
        turt.goto(position)
        self.segments.append(turt)


    def extend(self):
        self.add_seg(self.segments[-1].position())

    def move(self):
        for segnum in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[segnum - 1].xcor()
            newy = self.segments[segnum - 1].ycor()
            self.segments[segnum].goto(newx, newy)
        self.segments[0].fd(move_dis )

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)



