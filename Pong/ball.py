from turtle import Turtle
INITIAL_SPEED = 0.06

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = INITIAL_SPEED
        self.multiplier = 0.9

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_wall(self):
        self.y_move = -self.y_move

    def bounce_paddle(self):
        self.x_move = -self.x_move
        if self.move_speed <= 0.015:
            pass
        else:
            self.move_speed *= self.multiplier

    def score(self):
        self.goto(0,0)
        self.x_move = -self.x_move
        self.move_speed = INITIAL_SPEED