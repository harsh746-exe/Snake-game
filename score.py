from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")



class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("High_score.txt") as hs:
            self.high_score = int(hs.read())
        self.ht()
        self.pu()
        self.pencolor("blue")
        self.goto(0, 280)
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score = {self.current_score}  High Score = {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def new_score(self):
        self.current_score += 1
        self.clear()
        self.scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("High_score.txt", mode="w") as hs:
                hs.write(str(self.current_score))
            self.current_score = 0
            self.scoreboard()




