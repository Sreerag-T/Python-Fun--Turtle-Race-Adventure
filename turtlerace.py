from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput(title="Make Your Bet", prompt="Who will WIN?")
y_direction = 200
colors = ["red", "blue", "green", "orange", "purple", "yellow"]
turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-250, y=y_direction)
    y_direction -= 50
    turtles.append(new_turtle)

if user_bet:
    is_countinue = True
else:
    print("You Are Oomfi")

while is_countinue:
    for turtle in turtles:
        if turtle.xcor() >= 280:
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                is_countinue = False
                print(f"U WIN , {winning_color} color turtle Won the Race")
            else:
                print(f"U Loose , {winning_color} color turtle Won the Race")
                is_countinue = False
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()



