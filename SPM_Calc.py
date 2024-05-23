'''
---IMPORTANT!!!!---
1. Create branch guna nama korg
2. After save always :-
    a) git add .
    b) git commit -m "comment"
3. Make sure edit dkt branch bukan dkt main code
4. Kalau nak merge dgn main code, buat branch baru sbb takut tk jadi . so apa apa boleh pergi balik branch asal
'''
import math
import tkinter as tk
from tkinter import messagebox
from tkinter import *


from tkinter import ttk
import sqlite3

#test
window = tk.Tk()
window.title("Login form")

#utk dapatkan size screen
window.state("zoomed")
window.configure(bg='#212129')


def register(): #function utk kalau click register keluar page register
    global frame
    global register_frame
    frame.pack_forget()

    student_info_frame=tk.LabelFrame(register_frame, text="Student information",font=("Helvetica", 16),bg="#212129",fg="#FFFFFF")
    student_info_frame.grid(row=0,column=0,padx=20,pady=20)

    username_label_register=tk.Label(student_info_frame,text="Username",font=("Helvetica", 12),bg="#212129",fg="#FFFFFF")
    username_label_register.grid(row=0,column=0,padx=20,pady=10)
    password_label_register=tk.Label(student_info_frame,text="Password",font=("Helvetica", 12),bg="#212129",fg="#FFFFFF")
    password_label_register.grid(row=0,column=1)
    confirm_password_label=tk.Label(student_info_frame,text="Confirm password",font=("Helvetica", 12),bg="#212129",fg="#FFFFFF")
    confirm_password_label.grid(row=0,column=2)
    form_label=tk.Label(student_info_frame,text="Form",font=("Helvetica", 12),bg="#212129",fg="#FFFFFF")
    form_label.grid(row=3,column=0,padx=20,pady=10)
    class_label=tk.Label(student_info_frame,text="Class",font=("Helvetica", 12),bg="#212129",fg="#FFFFFF")
    class_label.grid(row=3,column=2)

    username_register_entry=tk.Entry(student_info_frame,font=("Helvetica", 12))
    password_register_entry=tk.Entry(student_info_frame,show="*",font=("Helvetica", 12))
    confirm_password_entry=tk.Entry(student_info_frame,show="*",font=("Helvetica", 12))
    username_register_entry.grid(row=1,column=0,padx=20,pady=10)
    password_register_entry.grid(row=1,column=1,padx=10,)
    confirm_password_entry.grid(row=1,column=2,padx=20)
    form_combobox=ttk.Combobox(student_info_frame,values=["4", "5"],font=("Helvetica", 12))
    form_combobox.grid(row=4,column=0,padx=20,pady=10)
    class_combobox=ttk.Combobox(student_info_frame,values=["Perdana", "Bestari", "Satria"],font=("Helvetica", 12))
    class_combobox.grid(row=4,column=2)
    
    def showPassword():
        if password_register_entry.cget("show")=="*" and confirm_password_entry.cget("show")=="*":
            password_register_entry.config(show='')
            confirm_password_entry.config(show='')
            show_button.update()
        else:
            password_register_entry.config(show="*")
            confirm_password_entry.config(show='*')
            show_button.update()
    
    def enter_data():
        global cursor
        global conn
        username=username_register_entry.get()
        password= password_register_entry.get()
        confirmPassword= confirm_password_entry.get()
        form= form_combobox.get()
        className=class_combobox.get()
    
        if username and password: #means if username and password if not empty strings
            if password != confirmPassword:
                messagebox.showerror(title="Error", message="Password didn't match")
            elif form and className:
                pass
            else:
                messagebox.showerror(title="Error", message="Form and class can't be empty")

            conn=sqlite3.connect("data.db")
            table_create_query='''CREATE TABLE IF NOT EXISTS Student_Data
                    (username TEXT, password TEXT, form INT, className TEXT)'''
            conn.execute(table_create_query)
            cursor=conn.cursor()

            #check if username and password already exist
            cursor.execute("SELECT * FROM Student_Data WHERE username=?",[username])
            result=cursor.fetchone()
            if result: #if result exists
                messagebox.showerror(title="Error", message="Account already exists")
      
            else:
                #insert data
                data_insert_query='''INSERT INTO Student_Data (username,password,form,className) VALUES (?,?,?,?)'''
                data_insert_tuple=(username, password, form, className) #tuple will replace the question mark
                cursor.execute(data_insert_query,data_insert_tuple) #means execute x and put y in your execution
                conn.commit() #use commit whenever insert data into sqlite database///penting utk save data in database
                messagebox.showinfo(title="Registered Succesfully", message="You successfully registered")



            conn.close()
            backbutton(register_frame,frame)



        else:
            messagebox.showerror(title="Error", message="Username and password can't be empty")


    #show/hide password
    show_button=Checkbutton(student_info_frame,text="Show password",selectcolor="#212129",command=showPassword,font=("Helvetica", 10),bg="#212129",fg="#08edff")
    show_button.update()
    show_button.grid(row=2,column=1)

    #enter data button
    signUp_button=tk.Button(register_frame,text="Confirm registration",command=enter_data,bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16))
    signUp_button.grid(row=5,padx=20,pady=5,sticky="EW")

    backRegister_button.grid (row=6,column=0,columnspan=2,padx=20,pady=5,sticky="EW")
    register_frame.pack()

def show_frame(frame):
    frame.tkraise()

def home_page():
    menu_frame = ttk.Frame(container, style="TFrame")
    menu_frame.grid(row=0, column=1, sticky="nsew")

    for i in range(3):
        menu_frame.rowconfigure(i, weight=1)
    menu_frame.columnconfigure(0, weight=1)

    label = ttk.Label(menu_frame, text="Choose a subject: ", font=("Arial", 24, "bold"), background="purple")
    label.grid(row=0, column=0, pady=20)

    button_frame = ttk.Frame(menu_frame, style="TFrame")
    button_frame.grid(row=1, column=0, pady=20)

    #button_style = ttk.Style()
    #button_style.configure('TButton', font=("Arial", 14), padding=10)

    physics_button = tk.Button(button_frame, text="Physics", font=("Arial", 18), bg="lightgreen", command=lambda: show_frame(pages["PhysicsPage"]))
    physics_button.grid(row=0, column=0, pady=10, padx=20, sticky='ew')

    chemistry_button = tk.Button(button_frame, text="Chemistry", font=('Arial', 18), bg="lightblue", command=lambda: show_frame(pages["ChemistryPage"]))
    chemistry_button.grid(row=1, column=0, pady=10, padx=20, sticky='ew')

    biology_button = tk.Button(button_frame, text="Biology", font=('Arial', 18), bg='lightcoral', command=lambda: show_frame(pages["BiologyPage"]))
    biology_button.grid(row=2, column=0, pady=10, padx=20, sticky='ew')

    button_frame.columnconfigure(0, weight=1)

    return menu_frame


def subject_page(subject_name):
    page = ttk.Frame(container, style='TFrame')
    pages[subject_name + "Page"] = page

    for i in range(3):
        page.rowconfigure(i, weight=1)
    page.columnconfigure(0, weight=1)

    label = ttk.Label(page, text = f"{subject_name} Formula Calculator", font = ("Arial", 20, "bold"), background="purple")
    label.grid(row=0, column=0, pady=20)

    back_button = tk.Button(page, text = "Back to Menu", font=("Arial", 18), bg="#5DEBD7", command = lambda: show_frame(pages["StartPage"]))
    back_button.grid(row=1, column=0, pady=20)

    page.columnconfigure(0, weight=1)

    page.grid(row=0, column=1, sticky="nsew")
    return page

#window = tk.Tk()
#window.title("SPM Formula Calculator")
#window.geometry("500x400")

container = ttk.Frame(window)
container.pack(fill="both", expand=True)

for i in range(3):
    container.rowconfigure(i, weight=1)
    container.columnconfigure(i, weight=1)

style= ttk.Style()
style.configure("TFrame", background="#212129")

pages = {}

pages["StartPage"] = home_page()

for subject in ["Physics", "Chemistry", "Biology"]:
    pages[subject + "Page"] = subject_page(subject)

show_frame(pages["StartPage"])

#window.mainloop()

def login(): #ni nanti kena connect dgn database sql kot

    global cursor
    global conn
    global afterLogin

    username=username_entry.get()
    password=password_entry.get()
    if username and password:
        conn=sqlite3.connect("data.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM Student_Data WHERE username=? AND password=?",[username,password])
        result=cursor.fetchall()
        if result == []:
            messagebox.showerror(title="Error", message="Account not found")
        else:
            print ("yay") #nanti letak function
            home_page()
            backbutton(frame,afterLogin_frame)

        conn.close()
    else:
        messagebox.showerror(title="Error", message="Username and password can't be empty")

def backbutton(forgetSurface,packSurface):
    forgetSurface.pack_forget()
    packSurface.pack()

#frames
frame = tk.Frame(bg='#212129')
register_frame=tk.Frame(bg="#212129")
afterLogin_frame=tk.Frame(bg="#212129")

# Creating widgets
login_label = tk.Label(frame, text="Login", bg='#212129', fg="#08edff", font=("Helvetica", 30))
username_label = tk.Label(frame, text="Username", bg='#212129', fg="#FFFFFF", font=("Helvetica", 16))
username_entry = tk.Entry(frame, font=("Helvetica", 16))
password_entry = tk.Entry(frame, show="*", font=("Helvetica", 16))
password_label = tk.Label(frame, text="Password", bg='#212129', fg="#FFFFFF", font=("Helvetica", 16))
login_button = tk.Button(frame, text="Login", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=login)
register_button = tk.Button(frame, text="Register", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=register)

backRegister_button = tk.Button(register_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(register_frame,frame))

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0,columnspan=2,padx=20,pady=5,sticky="EW" )
register_button.grid(row=4,column=0,columnspan=2,padx=20,pady=5,sticky="EW" )


frame.pack()

window.mainloop()

