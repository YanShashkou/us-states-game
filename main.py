import pandas
import turtle
from writer import Writer
screen = turtle.Screen()
image = 'blank_states_img.gif'
screen.addshape(image)
writer = Writer()
screen.title("States Game")
turtle.shape(image)
game_on = True
data = pandas.read_csv('50_states.csv')
all_states = data['state']
guessed_states =[]
while game_on:
    answer = screen.textinput(f'You have guessed {len(guessed_states)}/50',"Enter state name").title()
    for state in all_states:
        if state == answer:
            guessed_states.append(answer)
            state_line = data[data['state'] == state]
            print(state_line)
            x = int(state_line.x)
            y = int(state_line.y)
            writer.write_state(x,y,answer)







screen.exitonclick()