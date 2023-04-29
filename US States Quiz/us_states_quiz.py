from turtle import Turtle, Screen
import pandas as pd

background = Turtle()

writer = Turtle()
writer.penup()
writer.hideturtle()

screen = Screen()
screen.title("U.S. States Game")
#screen.setup()
image = "blank_states_img.gif"
screen.addshape(image)
background.shape(image)
df = pd.read_csv("50_states.csv")

# Variables
FONT = ("Consolas", 10, "normal")
states_list = df["state"].to_list()
states_x = df["x"]
states_y = df["y"]
score = 0
correct_guesses = []
states_to_learn = []

game_is_on = True
while game_is_on:
    if score == 0:
        answer = screen.textinput(title=f"Guess the state.", prompt="What's another state's name?").title()
    else:
        answer = screen.textinput(title=f"{score}/50 Guesses Right.", prompt="What's another state's name?").title()
    for state_number in range(0, 50):
        if answer == states_list[state_number]:
            score += 1
            x = states_x[state_number]
            y = states_y[state_number]
            writer.goto(x, y)
            writer.write(align="center", arg=states_list[state_number], font=FONT)
            correct_guesses.append(states_list[state_number])
    if len(correct_guesses) == 50:
        writer.home()
        writer.pencolor("turquoise1")
        writer.write(arg="Congrats, YOU WON!!!", align="center", font=("Consolas", 30, "normal"))
        game_is_on = False
    if answer == "Exit":

        for state in states_list:
            if state not in correct_guesses:
                states_to_learn.append(state)
        states_to_learn_df = pd.DataFrame(states_to_learn)
        states_to_learn_df.to_csv("states_to_learn.csv")
        break
