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

    button_options = {'font': ("Arial", 18), 'bg': 'lightgray', 'width': 10, 'height': 2}

    physics_button = tk.Button(button_frame, text="Physics", **button_options, command=lambda: show_frame(pages["PhysicsPage"]))
    physics_button.grid(row=0, column=0, pady=10, padx=20, sticky='ew')

    chemistry_button = tk.Button(button_frame, text="Chemistry", **button_options, command=lambda: show_frame(pages["ChemistryPage"]))
    chemistry_button.grid(row=1, column=0, pady=10, padx=20, sticky='ew')

    biology_button = tk.Button(button_frame, text="Biology", **button_options, command=lambda: show_frame(pages["BiologyPage"]))
    biology_button.grid(row=2, column=0, pady=10, padx=20, sticky='ew')

    button_frame.columnconfigure(0, weight=1)

    return menu_frame

def form_page(subject_name, form):
    page = ttk.Frame(container, style='TFrame')
    pages[subject_name + form + "Page"] = page

    for i in range(3):
        page.rowconfigure(i, weight=1)
    page.columnconfigure(0, weight=1)

    label = ttk.Label(page, text=f"{subject_name} - Form {form} Calculator", font=("Arial", 20, "bold"), background="purple")
    label.grid(row=0, column=0, pady=20)

    back_button = tk.Button(page, text="Back to Menu", font=("Arial", 18), bg="#5DEBD7", command=lambda: show_frame(pages[subject_name + "Page"]))
    back_button.grid(row=1, column=0, pady=20)

    button_options = {'font': ("Arial", 18), 'bg': 'lightgray', 'width': 10, 'height': 2}

    if form == '4':
        chapter_button = tk.Button(page, text="Chapter 1", **button_options, command=lambda: show_frame(pages[subject_name + "Form4Chapter1"]))
        chapter_button.grid(row=2, column=0, pady=10, padx=20, sticky='ew')
    elif form == '5':
        chapter_button = tk.Button(page, text="Chapter 1", **button_options, command=lambda: show_frame(pages[subject_name + "Form5Chapter1"]))
        chapter_button.grid(row=2, column=0, pady=10, padx=20, sticky='ew')

    page.columnconfigure(0, weight=1)
    page.grid(row=0, column=1, sticky="nsew")
    return page

def chapter_page(subject_name, form):
    page = ttk.Frame(container, style='TFrame')
    pages[subject_name + form + "Chapter1"] = page

    for i in range(5):
        page.rowconfigure(i, weight=1)
    for i in range(4):
        page.columnconfigure(i, weight=1)

    label = ttk.Label(page, text=f"{subject_name} - Form {form} Chapter 1", font=("Arial", 20, "bold"), background="purple")
    label.grid(row=0, column=1, columnspan=2, pady=20)

    back_button = tk.Button(page, text="Back to Form", font=("Arial", 18), bg="#5DEBD7", command=lambda: show_frame(pages[subject_name + form + "Page"]))
    back_button.grid(row=1, column=1, columnspan=2, pady=20)

    # Chapter-specific widgets (example: area calculation)
    label_enter_height = tk.Label(page, text='Enter Height', bg='#212129', fg="#08edff", font=('Arial', 15), pady=10)
    entry_enter_height = ttk.Entry(page)
    label_enter_width = tk.Label(page, text='Enter Width', bg='#212129', fg="#08edff", font=('Arial', 15), pady=10)
    entry_enter_width = ttk.Entry(page)
    button_calculate_area = ttk.Button(page, text='Calculate Area', command=lambda: calculate_area(entry_enter_height, entry_enter_width, label_area))
    label_area = tk.Label(page, text='Area', bg='#212129', fg="#08edff", font=('Arial', 15), pady=10)

    label_enter_height.grid(row=2, column=0, pady=10, sticky='e')
    entry_enter_height.grid(row=2, column=1, pady=10, sticky='w')
    label_enter_width.grid(row=2, column=2, pady=10, sticky='e')
    entry_enter_width.grid(row=2, column=3, pady=10, sticky='w')
    button_calculate_area.grid(row=3, column=1, columnspan=2, pady=10)
    label_area.grid(row=4, column=1, columnspan=2, pady=10)

    page.grid(row=0, column=1, sticky="nsew")
    return page

def subject_page(subject_name):
    page = ttk.Frame(container, style='TFrame')
    pages[subject_name + "Page"] = page

    for i in range(3):
        page.rowconfigure(i, weight=1)
    page.columnconfigure(0, weight=1)

    label = ttk.Label(page, text = f"{subject_name} Formula Calculator", font = ("Arial", 20, "bold"), background="purple")
    label.grid(row=0, column=0, pady=20)

    button_options = {'font': ("Arial", 18), bg: '#D3D3D3', 'width': 10, 'height': 2}

    form4_button = tk.Button(page, text="Form 4", **button_options, command=lambda: show_frame(pages[subject_name + "Form4Page"]))
    form4_button.grid(row=1, column=0, pady=10, padx=20, sticky='ew')

    form5_button = tk.Button(page, text="Form 5", **button_options, command=lambda: show_frame(pages[subject_name + "Form5Page"]))
    form5_button.grid(row=2, column=0, pady=10, padx=20, sticky='ew')

    back_button = tk.Button(page, text="Back to Menu", font=("Arial", 18), bg="#5DEBD7", command=lambda: show_frame(pages["StartPage"]))
    back_button.grid(row=3, column=0, pady=20)

    page.columnconfigure(0, weight=1)
    page.grid(row=0, column=1, sticky="nsew")
    return page 

window = tk.Tk()
window.title("SPM Formula Calculator")
window.geometry("600x400")

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