from turtle import Turtle
ALIGNEMENT="center"
FONT=("arial", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        # self.high_score=0
        with open("A:\project\Snake Game\data.txt",) as data:
            self.high_score=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,267)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", align=ALIGNEMENT, font=FONT)

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("A:\project\Snake Game\data.txt", mode="w") as data:
                data.write(f"{self.high_score}")    

        self.score=0 
        self.update_scoreboard()   


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNEMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()