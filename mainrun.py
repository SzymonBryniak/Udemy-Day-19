from turtle import Turtle, Screen

t = Turtle(shape="turtle")
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

t.penup()
t.goto(x=200, y=0)

screen.exitonclick()