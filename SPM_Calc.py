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

    form_4_window = tk.Frame(window, bg="#212129")
    form_5_window = tk.Frame(window, bg="#212129")
    c1_f4_window = tk.Frame(window, bg="#212129"  )
    c1_f5_window =tk.Frame(window, bg="#212129"  )

    form_4_window.grid(row=0, column=0, sticky='news')
    form_5_window.grid(row=0, column=0, sticky='news')
    c1_f4_window.grid (row=0, column=0, sticky='news') 
    c1_f5_window.grid(row=0, column=0, sticky='news') 

    window.title("SPM Calculator")
    window.geometry('500x500')
    window.configure(bg='#212129')

    frame = ttk.Frame(window)
    frame.grid(row=0, column=0, sticky='news')
    
    # Widgets
    label_spmcalculator = tk.Label(frame, text='SPM Calculator', bg='#212129', fg="#08edff", font=('Arial', 30), pady=40)
    form4_button = tk.Button(frame, text='Form 4', bg='#212129', fg="#08edff", font=('Arial', 20), padx=20, command=lambda: form_4_window.tkraise())
    form5_button = tk.Button(frame, text='Form 5', bg='#212129', fg='#08edff', font=('Arial', 20), padx=20, command=lambda: form_5_window.tkraise())
    back_button_form4 = tk.Button(form_4_window, text='Back', command=lambda: frame.tkraise())
    back_button_form5 = tk.Button(form_5_window, text='Back', command=lambda: frame.tkraise())
    chapter_1_button_form4 = tk.Button(form_4_window, text='chapter 1',command=lambda: c1_f4_window.tkraise())
    chapter_1_button_form5 = tk.Button(form_5_window, text='chapter 1', command=lambda: c1_f5_window.tkraise())
    back_button_chapter_to_form_4=tk.Button(c1_f4_window, text='back',command=lambda: form_4_window.tkraise())
    back_button_chapter_to_form_5=tk.Button(c1_f5_window, text='back',command=lambda: form_5_window.tkraise())
    
    
   #grid
    label_spmcalculator.grid(row=0, column=0, columnspan=2, pady=10, sticky='news')
    form4_button.grid(row=1, column=0, padx=10, pady=10)
    form5_button.grid(row=1, column=1, padx=10, pady=10)
    
    back_button_form4.grid(row=1, column=0,)
    back_button_form5.grid(row=1, column=0,)
    chapter_1_button_form4.grid(row=0, column=0,)
    chapter_1_button_form5.grid(row=0, column=0,)
    back_button_chapter_to_form_4.grid(row=0,column=0)
    back_button_chapter_to_form_5.grid(row=0,column=0)


    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    form_4_window.grid_columnconfigure(0, weight=1)
    form_4_window.grid_rowconfigure(0, weight=1)
    form_5_window.grid_columnconfigure(0, weight=1)
    form_5_window.grid_rowconfigure(0, weight=1)


    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=1)
    
    frame.tkraise()

    window.mainloop()





