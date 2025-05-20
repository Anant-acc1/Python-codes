from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,265)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode='w') as data:
                data.write(str(self.high_score))
        self.score = 0

    def score_increase(self):
        self.score += 1
        self.update_scoreboard()