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
    menu_frame.grid(row=0, column=0, sticky="nsew")

    label = ttk.Label(menu_frame, text="Choose a subject: ", font=("Arial", 18, "bold"), background="purple")
    label.grid(row=0, column=0, pady=20)

    button_frame = ttk.Frame(menu_frame, style="TFrame")
    button_frame.grid(row=1, column=0, pady=20)

    #button_style = ttk.Style()
    #button_style.configure('TButton', font=("Arial", 14), padding=10)

    physics_button = tk.Button(button_frame, text="Physics", font=("Arial", 14), bg="lightgreen", command=lambda: show_frame(pages["PhysicsPage"]))
    physics_button.pack(row=0, column=0, pady=5, sticky='ew')

    chemistry_button = tk.Button(button_frame, text="Chemistry", font=('Arial', 14), bg="lightblue", command=lambda: show_frame(pages["ChemistryPage"]))
    chemistry_button.pack(row=1, column=0, pady=5, sticky='ew')

    biology_button = tk.Button(button_frame, text="Biology", font=('Arial', 14), bg='lightcoral', command=lambda: show_frame(pages["BiologyPage"]))
    biology_button.pack(row=2, column=0, pady=5, sticky='ew')

    button_frame.columnconfigure(0, weight=1)

    return menu_frame

def subject_page(subject_name):
    page = ttk.Frame(container, style='TFrame')
    pages[subject_name + "Page"] = page

    label = ttk.Label(page, text = f"{subject_name} Formula Calculator", font = ("Arial", 16, "bold"), background="purple")
    label.pack(pady=20)

    back_button = tk.Button(page, text = "Back to Menu", font=("Arial", 14), bg="#212129", command = lambda: show_frame(pages["StartPage"]))
    back_button.pack(row=1, column=0, pady=20)

    

    page.grid(row=0, column=0, sticky="nsew")
    return page

window = tk.Tk()
window.title("SPM Formula Calculator")
window.geometry("400x300")

container = ttk.Frame(window)
container.pack(fill="both", expand=True)

pages = {}

pages["StartPage"] = home_page()

for subject in ["Physics", "Chemistry", "Biology"]:
    pages[subject + "Page"] = subject_page(subject)

show_frame(pages["StartPage"])

window.mainloop()