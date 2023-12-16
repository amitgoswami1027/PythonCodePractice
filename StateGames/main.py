import turtle
import pandas

#Concatinate the file paths
#file ="C:\Storage\AmitGoswami\Github\PythonCodePractice\StateGames\blank_states_img.gif"
image = "C:\Storage\AmitGoswami\Github\PythonCodePractice\StateGames\/blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S States Games")
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title= "Guess the state", prompt = "Whats the another state name")
print(answer_state)

#Check if answer state is one of the state in the list of 50 states given
data = pandas.read_csv("C:\Storage\AmitGoswami\Github\PythonCodePractice\StateGames\/50_states.csv")
all_states = data.state.to_list()

if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(state_data.state)

def get_mouse_click_coordinates(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coordinates)
turtle.mainloop()



#screen.exitonclick()
