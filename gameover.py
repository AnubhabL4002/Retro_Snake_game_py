from turtle import Turtle

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 0)

    def game_over_display(self):
        """it displays the game over screen when any bad collision occurs."""
        self.write("Game Over.", align="center", font= ('SH pinscher',25,'normal'))

