'''
---IMPORTANT!!!!---
1. Create branch guna nama korg
2. After save always :-
    a) git add .
    b) git commit -m "comment"
3. Make sure edit dkt branch bukan dkt main code
4. Kalau nak merge dgn main code, buat branch baru sbb takut tk jadi . so apa apa boleh pergi balik branch asal
'''

import tkinter as tk
from tkinter import ttk

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

    back_button = tk.Button(page, text = "Back to Menu", font=("Arial", 18), bg="#3EA99F", command = lambda: show_frame(pages["StartPage"]))
    back_button.grid(row=1, column=0, pady=20)

    page.columnconfigure(0, weight=1)

    page.grid(row=0, column=1, sticky="nsew")
    return page

window = tk.Tk()
window.title("SPM Formula Calculator")
window.geometry("500x400")

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

window.mainloop()