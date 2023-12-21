from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("C:\Storage\AmitGoswami\Github\PythonCodePractice\MyPasswordManager\data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File Not Found Error")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\n Password:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No data for the {website} exists")


#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    passwork_entry.insert(0,password)
    pyperclip.copy(password)
    

    print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    website = website_entry.get()
    email = email_entry.get()
    passwd = passwork_entry.get()

   #Using txt file to write the information
   # if len(website) == 0 or len(passwd) == 0:
   #     messagebox.showinfo(title=website, message="Please enter all the mandatory fields.")
   # else:
   #     is_ok = messagebox.askokcancel(title=website, message=f"These are the inputs enteres website : {website}\n" 
   #                                                 f"email:{email}\n and Password:{passwd}\n Is it Ok to save")

   #     if is_ok:
   #         with open("C:\Storage\AmitGoswami\Github\PythonCodePractice\MyPasswordManager\data.txt","a") as data_file:
   #             data_file.write(f"{website}|{email}|{passwd}\n")
   #             website_entry.delete(0,END)
   #             email_entry.delete(0,END)
   #             passwork_entry.delete(0,END)

    new_data = {
        website: {
            "email" : email,
            "password" : passwd
        }
    }

    # Using json file to write the information
    if len(website) == 0 or len(passwd) == 0:
        messagebox.showinfo(title=website, message="Please enter all the mandatory fields.")
    else:
        try:
            with open("C:\Storage\AmitGoswami\Github\PythonCodePractice\MyPasswordManager\data.json","r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("C:\Storage\AmitGoswami\Github\PythonCodePractice\MyPasswordManager\data.json","w") as data_file:
                json.dump(new_data,data_file, indent=4)
        else:
            data.update(new_data)

            with open("C:\Storage\AmitGoswami\Github\PythonCodePractice\MyPasswordManager\data.json","w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            passwork_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Manager")
window.config(padx=40,pady=40)

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="C:\Storage\AmitGoswami\Github\PythonCodePractice\MyPasswordManager\logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

#labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_entry = Entry(width=38)
email_entry.insert(0,"amit@gmail.com")
email_entry.grid(row=2, column=1,columnspan=2)

passwork_entry = Entry(width=21)
passwork_entry.grid(row=3,column=1)

#Buttons
search_button = Button(text="Search", width = 18,command = find_password)
search_button.grid(row=1,column=2)
generate_password_button = Button(text="Generate Password",width=18, command=generate_password)
generate_password_button.grid(row=3,column=2)

add_button = Button(text="Add",width=36, command=save)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()