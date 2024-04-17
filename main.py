import turtle
import csv
import pandas


screen = turtle.Screen()
screen.title("US States-Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answer_state = screen.textinput(title="US STATES GAME", prompt="What's another states name: ").title()

data = pandas.read_csv("50_states.csv")

states = data["state"].tolist()
x_cor = data["x"]
y_cor = data["y"]


def x_cor(xcor):
    x = data[xcor]
    return x

# states_below_0 = data[data.x < 0]
# print(states_below_0)
#
# states_above_0 = data[data.x > 0]
# print(states_above_0)

game_is_on = True

while game_is_on:
    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


# for state in states:
#     if answer_state == state:
#         print(state)
#         print("it worked")
#     else:
#         print("wrong")


screen.mainloop()