from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align="center",font=("Courier",80,"normal"))

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1

    def winner(self):
        self.goto(0, 25)
        self.write("Game Over", align="center", font=("Courier", 40, "bold"))
        self.goto(0, -25)
        if self.l_score > 10:
            self.write("left player wins", align="center", font=("Courier", 40, "bold"))
        elif self.r_score > 10:
            self.write("right player wins", align="center", font=("Courier", 40, "bold"))