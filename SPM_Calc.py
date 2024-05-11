'''
---IMPORTANT!!!!---
1. Create branch guna nama korg
2. After save always :-
    a) git add .
    b) git commit -m "comment"
3. Make sure edit dkt branch bukan dkt main code
4. Kalau nak merge dgn main code, buat branch baru sbb takut tk jadi . so apa apa boleh pergi balik branch asal
'''
from tkinter import Tk, Label, Button
#test
root = Tk()

myLabel1 = Label(root, text='spm formula calculator')
myLabel2 = Label(root, text='Subjects')
myLabel1.grid (row = 0,column=0)
myLabel2.grid (row = 0,column=1)

backButton = Button(root, text='back')
backButton.grid(row =1, column=1)
root.mainloop()