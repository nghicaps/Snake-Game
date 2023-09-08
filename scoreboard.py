from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 15, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            self.highscore = int(f.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(
            f"Score: {self.score}\t\tHigh Score: {self.highscore}", False, ALIGN, FONT
        )

    def scoring(self):
        self.score += 1
        self.check_highscore()
        self.update()

    def check_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as f:
                f.write(str(self.highscore))

    def reset(self):
        self.score = 0
        self.update()
