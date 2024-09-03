from turtle import Turtle
score_pos = (0,250)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.score = 0
        self.speed('fastest')
        self.display_score()

    def display_score(self):
        self.sety(270)
        self.clear()
        self.write(f"Score: {self.score}", False, 'center', ('Arial', 13, 'normal'))

    def game_over(self):
        self.sety(0)
        self.write("GAME OVER", False, 'center', ('Arial', 20, 'normal'))

