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

    frame =tkinter.Frame(window)
    frame.pack()

    label = tkinter.Label (window, text='spm calculator')
    label.pack

    window.mainloop()



