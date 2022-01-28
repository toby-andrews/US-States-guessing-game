from turtle import Screen
import turtle
import pandas as pd
from write import Write

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
data_dict = data.to_dict()

all_states = data.state.tolist()

guessed_states = []
score = 0
while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another State's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in all_states:
        if answer_state in guessed_states:
            pass
        else:
            guessed_states.append(answer_state)
            state_num = (all_states.index(answer_state))
            x = (data_dict["x"][state_num])
            y = (data_dict["y"][state_num])
            write = Write(answer_state, (x, y))
            score += 1

set_difference = set(all_states) - set(guessed_states)
list_difference = list(sorted(set_difference))
data = pd.DataFrame(list_difference)
data.to_csv("missed_states.csv")
