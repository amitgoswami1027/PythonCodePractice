#import tkinter
from tkinter import *

window=Tk()
window.title("My first GUI Project")
window.minsize(width=500,height=300)

#label
my_label = Label(text="I am a label", font =("Arial",24,"bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


#button
def button_click():
    print("I got clicked")
    new_text=input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command = button_click)
button.pack()


#Entry
input = Entry(width=10)
input.pack()

#Text
text = Text(height=5,width=30)
#Put the cursor into the text
text.focus()
#Add some text to begin with
text.insert(END,"Example of multiple entry")
print(text.get("1.0",END))
text.pack()

#Spinbox
def spinbox_used():
    #get the current value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_=0 , to=10, width=5,command = spinbox_used)
spinbox.pack()

#Scale
def scale_used(value):
    print(value)

scale = Scale(from_=0,to=100, command=scale_used)
scale.pack()


#Checkbox
def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is ON?",
                          variable =checked_state,
                           command=checkbutton_used)

checked_state.get()
checkbutton.pack()

#Radiobuttons
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1",
                           value =1, variable=radio_state, command= radio_state)
radiobutton2 = Radiobutton(text="Option2",
                           value =2, variable=radio_state, command= radio_state)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits =["Apple", "Grape", "Bannana"]
for item in fruits:
    listbox.insert(fruits.index(item),item)

listbox.bind("<<ListboxSelect>>", listbox_used)

listbox.pack()












window.mainloop()






