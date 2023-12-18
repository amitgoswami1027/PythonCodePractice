#import tkinter
from tkinter import *


def button_click():
    print("I got clicked")
    new_text=input.get()
    my_label.config(text=new_text)

window=Tk()
window.title("My first GUI Project")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

#label
my_label = Label(text="I am a label", font =("Arial",24,"bold"))
#my_label.pack()
#my_label.place(x,y)
my_label.grid(column=0,row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")

#button
button = Button(text="Click Me", command = button_click)
#button.pack()
button.grid(column=1,row=1)

#Entry
input = Entry(width=10)
#input.pack()
input.grid(column=2,row=2)

#Text
text = Text(height=5,width=30)
#Put the cursor into the text
text.focus()
#Add some text to begin with
text.insert(END,"Example of multiple entry")
print(text.get("1.0",END))
#text.pack()



window.mainloop()






