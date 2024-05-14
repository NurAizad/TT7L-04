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

if __name__ == '__main__':
    window=tkinter.Tk()
    window.title("spm calculator")
    window.geometry('600x400')
    window.configure(bg='#0317fc')

    frame =tkinter.Frame(window)
    frame.pack()

    #widgets
    label_spmcalculator = tkinter.Label (frame, text='spm calculator', bg='#FFFFFF', fg="#0317fc")
    form4_button = tkinter.Button (frame, text='form 4', bg='#FFFFFF', fg="#0317fc")
    form5_button = tkinter.Button (frame, text='form 5', bg='#FFFFFF',fg='#0317fc')

    #placing them
    label_spmcalculator.grid(row=0, column=0, columnspan=2)
    form4_button.grid(row=1, column=0)
    form5_button.grid(row=1, column=1)


    window.mainloop()



