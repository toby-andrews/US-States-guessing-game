from turtle import Turtle

FONT = ("Courier", 16, "normal")
ALIGNMENT = "center"


class Write(Turtle):
    def __init__(self, answer_state, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.state = answer_state
        self.goto(position)
        self.write(self.state, align=ALIGNMENT, font=FONT)
