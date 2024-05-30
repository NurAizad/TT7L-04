'''
---IMPORTANT!!!!---
1. Create branch guna nama korg
2. After save always :-
    a) git add .
    b) git commit -m "comment"
3. Make sure edit dkt branch bukan dkt main code
4. Kalau nak merge dgn main code, buat branch baru sbb takut tk jadi . so apa apa boleh pergi balik branch asal
'''
import math
import tkinter as tk
from tkinter import messagebox
from tkinter import *


from tkinter import ttk
import sqlite3

#test
window = tk.Tk()
window.title("Login form")

#utk dapatkan size screen
window.state("zoomed")
window.configure(bg='#212129')

#frames
frame = tk.Frame(bg='#212129')
register_frame=tk.Frame(bg="#212129")
subject_frame=tk.Frame(bg="#212129")
chem_frame=tk.Frame(bg="#212129")
bio_frame=tk.Frame(bg="#212129")

#physics
phy_frame=tk.Frame(bg="#212129")
phyf4_frame=tk.Frame(bg="#212129")
phyf4c2_frame=tk.Frame(bg="#212129")
speed_frame=tk.Frame(bg="#212129")
velocity_frame=tk.Frame(bg="#212129")
def register(): #function utk kalau click register keluar page register
    global frame
    global register_frame
    frame.pack_forget()

    student_info_frame=tk.LabelFrame(register_frame, text="Student information",font=("Helvetica", 16),bg="#212129",fg="#FFFFFF")
    student_info_frame.grid(row=0,column=0,padx=20,pady=20)

    username_label_register=tk.Label(student_info_frame,text="Username",font=("Helvetica", 12),bg="#212129",fg="#FFFFFF")
    username_label_register.grid(row=0,column=0,padx=20,pady=10)
    password_label_register=tk.Label(student_info_frame,text="Password",font=("Helvetica", 12),bg="#212129",fg="#FFFFFF")
    password_label_register.grid(row=0,column=1)
    confirm_password_label=tk.Label(student_info_frame,text="Confirm password",font=("Helvetica", 12),bg="#212129",fg="#FFFFFF")
    confirm_password_label.grid(row=0,column=2)
    form_label=tk.Label(student_info_frame,text="Form",font=("Helvetica", 12),bg="#212129",fg="#FFFFFF")
    form_label.grid(row=3,column=0,padx=20,pady=10)
    class_label=tk.Label(student_info_frame,text="Class",font=("Helvetica", 12),bg="#212129",fg="#FFFFFF")
    class_label.grid(row=3,column=2)

    username_register_entry=tk.Entry(student_info_frame,font=("Helvetica", 12))
    password_register_entry=tk.Entry(student_info_frame,show="*",font=("Helvetica", 12))
    confirm_password_entry=tk.Entry(student_info_frame,show="*",font=("Helvetica", 12))
    username_register_entry.grid(row=1,column=0,padx=20,pady=10)
    password_register_entry.grid(row=1,column=1,padx=10,)
    confirm_password_entry.grid(row=1,column=2,padx=20)
    form_combobox=ttk.Combobox(student_info_frame,values=["4", "5"],font=("Helvetica", 12))
    form_combobox.grid(row=4,column=0,padx=20,pady=10)
    class_combobox=ttk.Combobox(student_info_frame,values=["Perdana", "Bestari", "Satria"],font=("Helvetica", 12))
    class_combobox.grid(row=4,column=2)
    
    def showPassword():
        if password_register_entry.cget("show")=="*" and confirm_password_entry.cget("show")=="*":
            password_register_entry.config(show='')
            confirm_password_entry.config(show='')
            show_button.update()
        else:
            password_register_entry.config(show="*")
            confirm_password_entry.config(show='*')
            show_button.update()
    
    def enter_data():
        global cursor
        global conn
        username=username_register_entry.get()
        password= password_register_entry.get()
        confirmPassword= confirm_password_entry.get()
        form= form_combobox.get()
        className=class_combobox.get()
    
        if username and password: #means if username and password if not empty strings
            if password != confirmPassword:
                messagebox.showerror(title="Error", message="Password didn't match")
            elif form and className:
                pass
            else:
                messagebox.showerror(title="Error", message="Form and class can't be empty")

            conn=sqlite3.connect("data.db")
            table_create_query='''CREATE TABLE IF NOT EXISTS Student_Data
                    (username TEXT, password TEXT, form INT, className TEXT)'''
            conn.execute(table_create_query)
            cursor=conn.cursor()

            #check if username and password already exist
            cursor.execute("SELECT * FROM Student_Data WHERE username=?",[username])
            result=cursor.fetchone()
            if result: #if result exists
                messagebox.showerror(title="Error", message="Account already exists")
      
            else:
                #insert data
                data_insert_query='''INSERT INTO Student_Data (username,password,form,className) VALUES (?,?,?,?)'''
                data_insert_tuple=(username, password, form, className) #tuple will replace the question mark
                cursor.execute(data_insert_query,data_insert_tuple) #means execute x and put y in your execution
                conn.commit() #use commit whenever insert data into sqlite database///penting utk save data in database
                messagebox.showinfo(title="Registered Succesfully", message="You successfully registered")



            conn.close()
            backbutton(register_frame,frame)



        else:
            messagebox.showerror(title="Error", message="Username and password can't be empty")


    #show/hide password
    show_button=Checkbutton(student_info_frame,text="Show password",selectcolor="#212129",command=showPassword,font=("Helvetica", 10),bg="#212129",fg="#08edff")
    show_button.update()
    show_button.grid(row=2,column=1)

    #enter data button
    signUp_button=tk.Button(register_frame,text="Confirm registration",command=enter_data,bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16))
    signUp_button.grid(row=5,padx=20,pady=5,sticky="EW")

    backRegister_button.grid (row=6,column=0,columnspan=2,padx=20,pady=5,sticky="EW")
    register_frame.pack()



def login(): #ni nanti kena connect dgn database sql kot

    global cursor
    global conn

    username=username_entry.get()
    password=password_entry.get()
    if username and password:
        conn=sqlite3.connect("data.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM Student_Data WHERE username=? AND password=?",[username,password])
        result=cursor.fetchall()
        if result == []:
            messagebox.showerror(title="Error", message="Account not found")
        else:
            print ("yay") #nanti letak function
            backbutton(frame,subject_frame)
            def PhysicsPage():
                backbutton(subject_frame,phy_frame)
                def phy_f4():
                    backbutton(phy_frame,phyf4_frame)
                    def phy_f4_chap2():
                        backbutton(phyf4_frame,phyf4c2_frame)
                        def speed():
                            backbutton(phyf4c2_frame,speed_frame)
                            def speed_calc():
                                distance=float(distance_entry.get())
                                time = float(time_entry.get())
                                speed=distance/time
                                result_label.config(text=f"Speed: {speed}")


                            speed_label=tk.Label(speed_frame, text="Physics Form 4 Chapter 2", bg="#212129",fg="#08edff",font=("Helvetica",34))
                            distance_label=tk.Label(speed_frame,text="Distance",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                            time_label=tk.Label(speed_frame,text="Time taken",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                            result_label=tk.Label(speed_frame,text="Speed: ",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                            distance_entry=tk.Entry(speed_frame, font=("Helvetica", 16))
                            time_entry=tk.Entry(speed_frame, font=("Helvetica", 16))

                            speed_back=tk.Button(speed_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(speed_frame,phyf4c2_frame))
                            speed_back.grid(row=9,column=1,pady=10)
                            calculate_button=tk.Button(speed_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:speed_calc())
                            calculate_button.grid(row=8,column=1,pady=10)


                            speed_label.grid(row=0,column=1,pady=10)
                            distance_label.grid(row=1,column=0,pady=10)
                            time_label.grid(row=2,column=0,pady=10)
                            distance_entry.grid(row=1,column=2)
                            time_entry.grid(row=2,column=2)
                            result_label.grid(row=3,column=1,pady=10)

                        def velocity():
                            backbutton(phyf4c2_frame,velocity_frame)
                            def velocity_calc():
                                displacement=float(displacement_entry.get())
                                time = float(time_entry.get())
                                velocity=displacement/time
                                result_label.config(text=f"Speed: {velocity}")


                            velocity_label=tk.Label(velocity_frame, text="Physics Form 4 Chapter 2", bg="#212129",fg="#08edff",font=("Helvetica",34))
                            displacement_label=tk.Label(velocity_frame,text="Displacement",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                            time_label=tk.Label(velocity_frame,text="Time taken",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                            result_label=tk.Label(velocity_frame,text="Velocity: ",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                            displacement_entry=tk.Entry(velocity_frame, font=("Helvetica", 16))
                            time_entry=tk.Entry(velocity_frame, font=("Helvetica", 16))

                            velocity_back=tk.Button(velocity_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(velocity_frame,phyf4c2_frame))
                            velocity_back.grid(row=9,column=1,pady=10)
                            calculate_button=tk.Button(velocity_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:velocity_calc())
                            calculate_button.grid(row=8,column=1,pady=10)


                            velocity_label.grid(row=0,column=1,pady=10)
                            displacement_label.grid(row=1,column=0,pady=10)
                            time_label.grid(row=2,column=0,pady=10)
                            displacement_entry.grid(row=1,column=2)
                            time_entry.grid(row=2,column=2)
                            result_label.grid(row=3,column=1,pady=10)

                        
                        
                        f4Chapter2_label=tk.Label(phyf4c2_frame, text="Physics Form 4 Chapter 2", bg="#212129",fg="#08edff",font=("Helvetica",34))
                        speed_button=tk.Button(phyf4c2_frame,text="Speed",bg="#90ee90", font=("Helvetica",24),command=lambda:speed())
                        velocity_button=tk.Button(phyf4c2_frame,text="Velocity",bg="#90ee90", font=("Helvetica",24),command=lambda:velocity())
                        acceleration_button=tk.Button(phyf4c2_frame,text="Acceleration",bg="#90ee90", font=("Helvetica",24))
                        momentum_button=tk.Button(phyf4c2_frame,text="Momentum",bg="#90ee90", font=("Helvetica",24))
                        force_button=tk.Button(phyf4c2_frame,text="Force",bg="#90ee90", font=("Helvetica",24))
                        impulse_button=tk.Button(phyf4c2_frame,text="Impulse",bg="#90ee90", font=("Helvetica",24))
                        impulsive_force_button=tk.Button(phyf4c2_frame,text="Impulsive Force",bg="#90ee90", font=("Helvetica",24))
                        weight_button=tk.Button(phyf4c2_frame,text="Weight",bg="#90ee90", font=("Helvetica",24))

                        phy_f4c2_back=tk.Button(phyf4c2_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(phyf4c2_frame,phyf4_frame))
                        phy_f4c2_back.grid(row=9,column=1,pady=10)


                        f4Chapter2_label.grid(row=0,column=1,pady=10)
                        speed_button.grid(row=1,column=1,pady=10,sticky="ew")          
                        velocity_button.grid(row=2,column=1,pady=10,sticky="ew")          
                        acceleration_button.grid(row=3,column=1,pady=10,sticky="ew")       
                        momentum_button.grid(row=4,column=1,pady=10,sticky="ew")      
                        force_button.grid(row=5,column=1,pady=10,sticky="ew")        
                        impulse_button.grid(row=6,column=1,pady=10,sticky="ew")       
                        impulsive_force_button.grid(row=7,column=1,pady=10,sticky="ew")    
                        weight_button.grid(row=8,column=1,pady=10,sticky="ew")              
                        


                    f4Chapter_label=tk.Label(phyf4_frame, text="Physics Form 4", bg="#212129",fg="#08edff",font=("Helvetica",34))
                    chap2_button=tk.Button(phyf4_frame,text="Chapter 2",bg="#90ee90", font=("Helvetica",24),command=lambda:phy_f4_chap2())
                    chap3_button=tk.Button(phyf4_frame,text="Chapter 3",bg="#90ee90", font=("Helvetica",24))
                    chap4_button=tk.Button(phyf4_frame,text="Chapter 4",bg="#90ee90", font=("Helvetica",24))
                    chap5_button=tk.Button(phyf4_frame,text="Chapter 5",bg="#90ee90", font=("Helvetica",24))
                    chap6_button=tk.Button(phyf4_frame,text="Chapter 6",bg="#90ee90", font=("Helvetica",24))

                    phy_f4_back=tk.Button(phyf4_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(phyf4_frame,phy_frame))
                    phy_f4_back.grid(row=6,column=2,pady=10)

                    f4Chapter_label.grid(row=0,column=2,padx=10,pady=10)
                    chap2_button.grid(row=1,column=0,padx=10,pady=50)
                    chap3_button.grid(row=1,column=2,padx=10)
                    chap4_button.grid(row=1,column=4,padx=10)
                    chap5_button.grid(row=2,column=1,padx=10,pady=50)
                    chap6_button.grid(row=2,column=3,padx=10)

                form4_button=tk.Button(phy_frame,text="Form 4", bg="#90ee90", font=("Helvetica",24), command=lambda:phy_f4())
                form5_button=tk.Button(phy_frame,text="Form 5", bg="#90ee90", font=("Helvetica",24))
                chooseForm_label=tk.Label(phy_frame,text="Choose which form:",bg="#212129",fg="#08edff", font=("Helvetica",34))

                phy_back = tk.Button(phy_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(phy_frame,subject_frame))

                form4_button.grid(row=1,column=0,padx=5,pady=200)
                form5_button.grid(row=1,column=2,padx=5)
                chooseForm_label.grid(row=0,column=1,sticky="ew",padx=10,pady=10)
                phy_back.grid(row=6,column=1)

            subject_label = tk.Label(subject_frame, text="Choose a subject", bg="#212129",fg="#08edff", font=("Helvetica",34))

            phy_button = tk.Button(subject_frame, text="Physics", bg="#90ee90", font=("Helvetica",24),command=lambda:PhysicsPage())
            chem_button = tk.Button(subject_frame, text="Chemistry", bg="#add8e6", font=("Helvetica",24))
            bio_button = tk.Button(subject_frame, text="Biology", bg="#f08080", font=("Helvetica",24))

            subject_back = tk.Button(subject_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(subject_frame,frame))

            subject_label.grid(row=0,column=1,columnspan=2,sticky="news",pady=40)
            subject_back.grid(row=6,column=1,columnspan=2,padx=20,pady=40)
            phy_button.grid(row=1,column=1,columnspan=2,padx=20,pady=20,sticky="ew")
            chem_button.grid(row=2,column=1,columnspan=2,padx=20,pady=20,sticky="ew")
            bio_button.grid(row=3,column=1,columnspan=2,padx=20,pady=20,sticky="ew")
            
                
        conn.close()
    else:
        messagebox.showerror(title="Error", message="Username and password can't be empty")

def backbutton(forgetSurface,packSurface):
    forgetSurface.pack_forget()
    packSurface.pack()



# Creating widgets
login_label = tk.Label(frame, text="Login", bg='#212129', fg="#08edff", font=("Helvetica", 34))
username_label = tk.Label(frame, text="Username", bg='#212129', fg="#FFFFFF", font=("Helvetica", 16))
username_entry = tk.Entry(frame, font=("Helvetica", 16))
password_entry = tk.Entry(frame, show="*", font=("Helvetica", 16))
password_label = tk.Label(frame, text="Password", bg='#212129', fg="#FFFFFF", font=("Helvetica", 16))
login_button = tk.Button(frame, text="Login", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=login)
register_button = tk.Button(frame, text="Register", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=register)

backRegister_button = tk.Button(register_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(register_frame,frame))

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0,columnspan=2,padx=20,pady=5,sticky="EW" )
register_button.grid(row=4,column=0,columnspan=2,padx=20,pady=5,sticky="EW" )


frame.pack()

window.mainloop()

