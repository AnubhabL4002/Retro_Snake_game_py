from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,260)

    def show_score(self):
        """it displays the score"""
        self.write(f"Score:  {self.score}", align="center", font= ('SH pinscher',25,'normal'))

    def update_score(self):
        """it updates the score when a fruit is eaten."""
        self.clear()
        self.score+=1
        self.write(f"Score:  {self.score}", align="center", font= ('SH pinscher',25,'normal'))
