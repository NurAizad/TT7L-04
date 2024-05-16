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

class SubjectCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SPM Formula Calculator")
        self.geometry("400x300")

        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        subjects = (StartPage, PhysicsPage, ChemistryPage, BiologyPage)

        for F in subjects:
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Select a Subject:", font=("Arial", 18, "bold"))
        label.pack(pady=20)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=20)

        button_style = ttk.Style()
        button_style.configure('TButton', font=("Arial", 14), padding=10)

        physics_button = ttk.Button(button_frame, text="Physics", style='TButton',
                                    command=lambda: controller.show_frame("PhysicsPage"))
        physics_button.pack(fill='x', pady=5)

        chemistry_button = ttk.Button(button_frame, text="Chemistry", style='TButton',
                                      command=lambda: controller.show_frame("ChemistryPage"))
        chemistry_button.pack(fill='x', pady=5)

        biology_button = ttk.Button(button_frame, text="Biology", style='TButton',
                                     command=lambda: controller.show_frame("BiologyPage"))
        biology_button.pack(fill='x', pady=5)

class PhysicsPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Physics Formula Calculator", font=("Arial", 16, "bold"))
        label.pack(pady=20)

        back_button = ttk.Button(self, text="Back to Home",
                                 command=lambda: controller.show_frame("StartPage"))
        back_button.pack(pady=20)

class ChemistryPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Chemistry Formula Calculator", font=("Arial", 16, "bold"))
        label.pack(pady=20)

        back_button = ttk.Button(self, text="Back to Home",
                                 command=lambda: controller.show_frame("StartPage"))
        back_button.pack(pady=20)

class BiologyPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Biology Formula Calculator", font=("Arial", 16, "bold"))
        label.pack(pady=20)

        back_button = ttk.Button(self, text="Back to Home",
                                 command=lambda: controller.show_frame("StartPage"))
        back_button.pack(pady=20)

if __name__ == "__main__":
    app = SubjectCalculator()
    app.mainloop()
