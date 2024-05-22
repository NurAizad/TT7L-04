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
    menu_frame = ttk.Frame(container)
    home_frame.grid(row=0, column=0, sticky="nsew")

    label = ttk.Label(home_frame, text="Choose a subject: ", font=("Arial", 18, "bold"))
    label.pack(pady = 20)


def subject_page(subject_name):
    page = tk.Frame(window)
    pages[subject_name] = page

    label = tk.Label(page, text = f"{subject_name} Formula Calculator", font = ("Manrope", 17, "bold"))
    label.pack()

    back_button = tk.Button(page, text = "Back to Menu", command = lambda: show_frame(menu_frame))
    back_button.pack()

    page.grid(row=0, column=0, sticky="nsew")
    return page

window = tk.Tk()
window.title("SPM Formula Calculator")
window.geometry("400x300")

container = ttk.Frame(window)
container.pack(fill="both", expand=True)

pages = {}

menu_frame = tk.Frame(window)
menu_frame.grid(row=0, column=0, sticky="nsew")

menu_label = tk.Label(menu_frame, text = "Choose a subject:", font = ("Manrope", 19, "bold"))
menu_label.pack() 

button_style = ttk.Style()
button_style.configure('TButton', font = "Manrope", padding = 10)

subjects = ["Physics", "Biology", "Chemistry"]
for subject in subjects:
    buttons = tk.Button(menu_frame, text=subject, font = ("Manrope, 15"), command=lambda s=subject: show_frame(pages[s]))
    buttons.pack(fill='x', pady = 5)


for subjects in subjects:
    subject_page(subjects)





show_frame(menu_frame)
window.mainloop()