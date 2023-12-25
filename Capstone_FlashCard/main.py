from tkinter import *
import pandas
import random

#Capstone Project - Amit Goswami
# Frequency List are the top vocab which used quite frequently.

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("C:\Storage\AmitGoswami\Github\PythonCodePractice\Capstone_FlashCard\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("C:\Storage\AmitGoswami\Github\PythonCodePractice\Capstone_FlashCard\data\/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")    

def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    #print(current_card["French"])
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word,text=current_card["French"])
    canvas.itemconfig(card_back_imag, image=card_front_imag)
    flip_timer=window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English")
    canvas.itemconfig(card_word,text=current_card["English"])
    canvas.itemconfig(card_back_imag,image=card_back_imag)

# Click Known Button
def is_known():
    to_learn.remove(current_card)
    next_word()
    data = pandas.DataFrame(to_learn)
    data.to_csv("C:\Storage\AmitGoswami\Github\PythonCodePractice\Capstone_FlashCard\words_to_learn.csv", index=False)
    next_word()

# Creating the UI of the Flash Card.
window = Tk()
window.title("My Flash Cards")
window.config(padx=50,pady=50,bg= BACKGROUND_COLOR)

# Weight for the 3 sec and flip the card
flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526)

card_front_imag = PhotoImage(file = "C:\Storage\AmitGoswami\Github\PythonCodePractice\Capstone_FlashCard\images\card_front.png")
card_back_imag = PhotoImage(file = "C:\Storage\AmitGoswami\Github\PythonCodePractice\Capstone_FlashCard\images\card_back.png")

canvas.create_image(400,263,image= card_front_imag)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400,150,text="",font = ("Arial",40, "italic"))
card_word = canvas.create_text(400,260,text="",font = ("Arial",60, "bold"))
canvas.grid(row=0,column=0,columnspan=2)

#Buttons 
#Wrong/Cancel Button
cross_image = PhotoImage(file = "C:\Storage\AmitGoswami\Github\PythonCodePractice\Capstone_FlashCard\images\wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0,command = next_word)
unknown_button.grid(row=1,column=0)

#Right/Correct Button
check_image = PhotoImage(file = "C:\Storage\AmitGoswami\Github\PythonCodePractice\Capstone_FlashCard\images\/right.png")
known_button = Button(image=check_image,highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)

next_word()

window.mainloop()