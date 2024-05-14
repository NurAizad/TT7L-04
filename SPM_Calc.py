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
import tkinter 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def open_form_4_window():
    form_4_window= tk.Toplevel()

def open_form_5_window():
    form_5_window= tk.Toplevel()

if __name__ == '__main__':
    window=tkinter.Tk()
    window.title("spm calculator")
    window.geometry('600x400')
    window.configure(bg='#0317fc')

    frame =tkinter.Frame(bg='#0317fc')
    

    #widgets
    label_spmcalculator = tkinter.Label (frame, text='spm calculator', bg='#0317fc', fg="#FFFFFF" , font='Arial, 30', pady=40)
    form4_button = tkinter.Button (frame, text='form 4', bg='#FFFFFF', fg="#0317fc", font='Arial, 20', padx=20, command=open_form_4_window)
    form5_button = tkinter.Button (frame, text='form 5', bg='#FFFFFF',fg='#0317fc', font='Arial, 20', padx=20, command=open_form_5_window)

    #placing them
    label_spmcalculator.grid(row=0, column=0, columnspan=2, sticky='news')
    form4_button.grid(row=1, column=0)
    form5_button.grid(row=1, column=1)
    frame.pack()


    window.mainloop()



