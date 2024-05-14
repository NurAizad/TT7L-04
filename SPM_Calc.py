'''
---IMPORTANT!!!!---
1. Create branch guna nama korg
2. After save always :-
    a) git add .
    b) git commit -m "comment"
3. Make sure edit dkt branch bukan dkt main code
4. Kalau nak merge dgn main code, buat branch baru sbb takut tk jadi . so apa apa boleh pergi balik branch asal
5. git push -u origin branchname
'''
import tkinter as tk
from tkinter import ttk

import tkinter as tk

if __name__ == '__main__':
    window = tk.Tk()

    form_4_window = tk.Frame(window)
    form_5_window = tk.Frame(window)

    form_4_window.grid(row=0, column=0, sticky='news')
    form_5_window.grid(row=0, column=0, sticky='news')

    window.title("SPM Calculator")
    window.geometry('600x400')
    window.configure(bg='#0317fc')

    frame = tk.Frame(window, bg='#0317fc')
    frame.grid(row=0, column=0, sticky='news')
    
    # Widgets
    label_spmcalculator = tk.Label(frame, text='SPM Calculator', bg='#0317fc', fg="#FFFFFF", font=('Arial', 30), pady=40)
    form4_button = tk.Button(frame, text='Form 4', bg='#FFFFFF', fg="#0317fc", font=('Arial', 20), padx=20, command=lambda: form_4_window.tkraise())
    form5_button = tk.Button(frame, text='Form 5', bg='#FFFFFF', fg='#0317fc', font=('Arial', 20), padx=20, command=lambda: form_5_window.tkraise())
    back_button_form4 = tk.Button(form_4_window, text='Back', command=lambda: frame.tkraise())
    back_button_form5 = tk.Button(form_5_window, text='Back', command=lambda: frame.tkraise())
    
    label_spmcalculator.grid(row=0, column=0, columnspan=2, sticky='news')
    form4_button.grid(row=1, column=0)
    form5_button.grid(row=1, column=1)
    
    back_button_form4.grid(row=0, column=0)
    back_button_form5.grid(row=0, column=0)
    
    frame.grid(row=0, column=0, sticky='news')
    frame.tkraise()

    window.mainloop()





