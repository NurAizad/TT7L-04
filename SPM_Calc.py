'''
---IMPORTANT!!!!---
1. Create branch guna nama korg
2. After save always :-
    a) git add .
    b) git commit -m "comment"
3. Make sure edit dkt branch bukan dkt main code
4. Kalau nak merge dgn main code, buat branch baru sbb takut tk jadi . so apa apa boleh pergi balik branch asal
'''

import tkinter

if __name__ == '__main__': 
    window = tkinter.Tk()
    window.title("SPM Formula Calculator")
    window.geometry('400x300')

    label = tkinter.Label(window, text = 'Hello Dunia')
    label.pack()
    button = tkinter.Button(window, text = 'testingg')
    button.pack()


    window.mainloop()

    print("Halo")