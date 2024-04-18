import turtle
import csv
import pandas

screen = turtle.Screen()
screen.title("US States-Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

states = data["state"].tolist()

while len(states) != 0:
    answer_state = screen.textinput(title=f"{len(states)} remain", prompt="What's another states name: ").title()
    if answer_state == "Exit":
        break
    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        states.remove(answer_state)


