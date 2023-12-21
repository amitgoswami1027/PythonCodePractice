from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("My Flash Cards")
window.config(padx=50,pady=50,bg= BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526)
card_front_imag = PhotoImage(file = "C:\Storage\AmitGoswami\Github\PythonCodePractice\Capstone_FlashCard\images\card_front.png")
canvas.create_image(400,263,image= card_front_imag)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400,150,text="Title",font = ("Arial",40, "italic"))
canvas.create_text(400,260,text="Word",font = ("Arial",60, "bold"))
canvas.grid(row=0,column=0,columnspan=2)

#Buttons
cross_image = PhotoImage(file = "C:\Storage\AmitGoswami\Github\PythonCodePractice\Capstone_FlashCard\images\wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file = "C:\Storage\AmitGoswami\Github\PythonCodePractice\Capstone_FlashCard\images\wrong.png")
unknown_button = Button(image=check_image,highlightthickness=0)
unknown_button.grid(row=1,column=1)



window.mainloop()