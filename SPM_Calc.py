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
    c9_f5_bio_window =tk.Frame(window, bg="#212129"  )
    c4_f4_bio_window =tk.Frame(window, bg="#212129" )
    c5_f4_bio_window = tk.Frame(window, bg="#212129"  )

    form_4_window.grid(row=0, column=0, sticky='news')
    form_5_window.grid(row=0, column=0, sticky='news')
    c5_f4_bio_window.grid (row=0, column=0, sticky='news') 
    c9_f5_bio_window.grid(row=0, column=0, sticky='news') 
    c4_f4_bio_window.grid (row=0, column=0, sticky='news') 

    window.title("SPM Calculator")
    window.geometry('500x500')
    window.configure(bg='#212129')

    frame = ttk.Frame(window)
    frame.grid(row=0, column=0, sticky='news')

    #functions

    def calculate_percentage_difference_in_mass():
       try:
          final_mass = int(entry_enter_final_mass.get())
          initial_mass = int(entry_enter_initial_mass.get())
          percentage_difference_in_mass = ((final_mass-initial_mass)/initial_mass)*0.01
          label_percentage_difference_in_mass.config(text=f"{percentage_difference_in_mass}")
       except ValueError:
        print("please enter numbers")  

    def calculate_enzyem_reaction_rate():
       try:
          time_taken=int(entry_time_taken.get())    
          enzyme_reaction_rate = 1/time_taken
          rounded_rate=round(enzyme_reaction_rate,4)
          label_enzyme_reaction_rate.config(text=f"{rounded_rate}")
       except ValueError:
          print('please enter numbers')  
       
    # Widgets main menu
    label_spmcalculator = tk.Label(frame, text='SPM Calculator', bg='#212129', fg="#08edff", font=('Arial', 30), pady=40)
    form4_button = tk.Button(frame, text='Form 4', bg='#212129', fg="#08edff", font=('Arial', 20), padx=20, command=lambda: form_4_window.tkraise())
    form5_button = tk.Button(frame, text='Form 5', bg='#212129', fg='#08edff', font=('Arial', 20), padx=20, command=lambda: form_5_window.tkraise())
    back_button_form4 = tk.Button(form_4_window, text='Back', command=lambda: frame.tkraise())
    back_button_form5 = tk.Button(form_5_window, text='Back', command=lambda: frame.tkraise())
    #widgets chapters f4 
    chapter_5_button_form4 = tk.Button(form_4_window, text='chapter 5',command=lambda: c5_f4_bio_window.tkraise())
    chapter_4_button_form4 =tk.Button(form_4_window, text='chapter 4',command=lambda: c4_f4_bio_window.tkraise())
    back_button_chapter4_to_form_4 = tk.Button(c4_f4_bio_window,text='back',command=lambda:form_4_window.tkraise())

    #widgets bio chapter 4 f4
    back_button_c4bio_to_form_4 =tk.Button(c4_f4_bio_window, text='back',command=lambda: form_4_window.tkraise())
    label_enter_final_mass = tk.Label(c4_f4_bio_window, text='enter final mass:',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
    entry_enter_final_mass = ttk.Entry(c4_f4_bio_window)
    label_enter_initial_mass = tk.Label(c4_f4_bio_window, text='enter initial mass:',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
    entry_enter_initial_mass = ttk.Entry(c4_f4_bio_window)
    label_percentage_difference_in_mass = tk.Label(c4_f4_bio_window, text='',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
    button_calculate_percentage_difference_in_mass = ttk.Button(c4_f4_bio_window, text='calculate percentage difference in mass', command=calculate_percentage_difference_in_mass)
    #widgets bio chapter 5 f4
    back_button_c5bio_to_form_4 =tk.Button(c5_f4_bio_window, text='back',command=lambda: form_4_window.tkraise())
    label_enter_time_taken = tk.Label(c5_f4_bio_window, text='enter time taken:',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
    entry_time_taken = ttk.Entry(c5_f4_bio_window)
    label_enzyme_reaction_rate = tk.Label(c5_f4_bio_window, text='',bg='#212129', fg="#08edff", font=('Arial', 15), pady=40)
    button_calculate_enzyme_reaction_rate = ttk.Button(c5_f4_bio_window, text='calcuate enzyme reaction rate', command=calculate_enzyem_reaction_rate)

    #widgets chapter f5
    chapter_9_button_form5 = tk.Button(form_5_window, text='chapter 9', command=lambda: c9_f5_bio_window.tkraise())
    back_button_chapter9_to_form_5=tk.Button(c9_f5_bio_window, text='back',command=lambda: form_5_window.tkraise())

    #grid chapters
    label_spmcalculator.grid(row=0, column=0, columnspan=2, pady=10, sticky='news')
    form4_button.grid(row=1, column=0, padx=10, pady=10)
    form5_button.grid(row=1, column=1, padx=10, pady=10)
    back_button_form4.grid(row=3, column=3,)
    back_button_form5.grid(row=2, column=2,)
    chapter_5_button_form4.grid(row=1, column=0,)
    chapter_4_button_form4.grid (row=0, column=0)
    chapter_9_button_form5.grid (row=0, column=0)
    
   #grid biolog c4 f4
    label_enter_final_mass.grid(row=0, column=0)
    entry_enter_final_mass.grid(row=0, column=1)
    label_enter_initial_mass.grid(row=1, column=0)
    entry_enter_initial_mass.grid(row=1, column=1)
    button_calculate_percentage_difference_in_mass.grid(row=2, column=0)
    label_percentage_difference_in_mass.grid(row=2, column=1)
    back_button_c4bio_to_form_4.grid (row=3, column=2)
    #grid biology c5 f4
    label_enter_time_taken.grid(row=0, column=0)
    entry_time_taken.grid(row=0, column=1)
    button_calculate_enzyme_reaction_rate.grid(row=2, column=0)
    back_button_c5bio_to_form_4.grid(row=3, column=2)
    label_enzyme_reaction_rate.grid(row=2, column=1)


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





