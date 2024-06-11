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
from PIL import Image, ImageTk

#test
window = tk.Tk()
window.title("Login form")

#utk dapatkan size screen
window.state("zoomed")
window.configure(bg='#212129')

#ni test gambar
screenWidth=window.winfo_screenwidth() #utk dptkan width window
screenHeight=window.winfo_screenheight()#dptkan height

BgImage=Image.open("images/class.jpg")
ResizeBgImage= BgImage.resize((screenWidth,screenHeight))
FinalBgImage=ImageTk.PhotoImage(ResizeBgImage)
BgImage_label=tk.Label(window,image=FinalBgImage)
BgImage_label.place(x=0,y=0)


#frames
frame = tk.Frame(bg='#212129')
register_frame=tk.Frame(bg="#212129")
subject_frame=tk.Frame(bg="#212129")
chem_frame=tk.Frame(bg="#212129")
bio_frame=tk.Frame(bg="#212129")
admin_frame=tk.Frame(bg="#212129")
adminInterface_frame=tk.Frame(bg="#212129")

#physics
phy_frame=tk.Frame(bg="#212129")
phyf4_frame=tk.Frame(bg="#212129")
phyf4c2_frame=tk.Frame(bg="#212129")
speed_frame=tk.Frame(bg="#212129")
velocity_frame=tk.Frame(bg="#212129")
acceleration_frame=tk.Frame(bg="#212129")
momentum_frame=tk.Frame(bg="#212129")
force_frame=tk.Frame(bg="#212129")
impulse_frame=tk.Frame(bg="#212129")
impulsiveForce_frame=tk.Frame(bg="#212129")
weight_frame=tk.Frame(bg="#212129")

#chemistry
chem_frame=tk.Frame(bg="#212129")
chemf4_frame=tk.Frame(bg="#212129")
chemf4c2_frame=tk.Frame(bg="#212129")
nucleon_frame=tk.Frame(bg="#212129")


def register(): #function utk kalau click register keluar page register
    global frame
    global register_frame
    #frame.pack_forget()

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

    backRegister_button.grid (row=6,column=0,columnspan=2,padx=20,pady=10,sticky="EW")
    backbutton(frame,register_frame)
    #register_frame.pack()

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
        elif result !=[] and username!= "admin" and password!="admin":
            backbutton(frame,subject_frame)
            subject_label = tk.Label(subject_frame, text="Choose a subject", bg="#212129",fg="#08edff", font=("Helvetica",34))

            phy_button = tk.Button(subject_frame, text="Physics", bg="#90ee90", font=("Helvetica",24),command=lambda:PhysicsPage(subject_frame,phy_frame))
            chem_button = tk.Button(subject_frame, text="Chemistry", bg="#add8e6", font=("Helvetica",24),command=lambda:ChemistryPage(subject_frame,chem_frame))
            bio_button = tk.Button(subject_frame, text="Biology", bg="#f08080", font=("Helvetica",24))

            subject_back = tk.Button(subject_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(subject_frame,frame))

            subject_label.grid(row=0,column=1,columnspan=2,sticky="news",padx=50,pady=40)
            subject_back.grid(row=6,column=1,columnspan=2,padx=20,pady=40)
            phy_button.grid(row=1,column=1,columnspan=2,padx=20,pady=20,sticky="ew")
            chem_button.grid(row=2,column=1,columnspan=2,padx=20,pady=20,sticky="ew")
            bio_button.grid(row=3,column=1,columnspan=2,padx=20,pady=20,sticky="ew")
        
        if username =="admin" and password=="admin":

            backbutton(frame,admin_frame)
            subject_label = tk.Label(admin_frame, text="Choose a subject", bg="#212129",fg="#08edff", font=("Helvetica",34))

            phy_button = tk.Button(admin_frame, text="Physics", bg="#90ee90", font=("Helvetica",24),command=lambda:PhysicsPage(admin_frame,phy_frame))
            chem_button = tk.Button(admin_frame, text="Chemistry", bg="#add8e6", font=("Helvetica",24),command=lambda:ChemistryPage(admin_frame,chem_frame))
            bio_button = tk.Button(admin_frame, text="Biology", bg="#f08080", font=("Helvetica",24))
            admin_button = tk.Button(admin_frame, text="Admin", bg="#b16eeb", font=("Helvetica",24),command=lambda:admin())

            subject_back = tk.Button(admin_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(admin_frame,frame))

            subject_label.grid(row=0,column=1,columnspan=2,sticky="news",pady=40)
            subject_back.grid(row=6,column=1,columnspan=2,padx=20,pady=40)
            phy_button.grid(row=1,column=1,columnspan=2,padx=20,pady=20,sticky="ew")
            chem_button.grid(row=2,column=1,columnspan=2,padx=20,pady=20,sticky="ew")
            bio_button.grid(row=3,column=1,columnspan=2,padx=20,pady=20,sticky="ew")
            admin_button.grid(row=4,column=1,columnspan=2,padx=20,pady=20,sticky="ew")
                
        conn.close()
    else:
        messagebox.showerror(title="Error", message="Username and password can't be empty")

def backbutton(forgetSurface,packSurface):
    forgetSurface.place_forget()
    packSurface.place(relx=0.5, rely=0.5,anchor='center')

def backbutton_delresult(forgetSurface,packSurface,result_label):
    result_label.config(text="")
    forgetSurface.place_forget()
    packSurface.place(relx=0.5, rely=0.5,anchor='center')

def PhysicsPage(forget_surface,pack_surface):
    #backbutton(subject_frame,phy_frame)
    backbutton(forget_surface,pack_surface)
    def phy_f4():
        backbutton(phy_frame,phyf4_frame)
        def phy_f4_chap2():
            backbutton(phyf4_frame,phyf4c2_frame)
            def speed():
                backbutton(phyf4c2_frame,speed_frame)
                def speed_calc():
                    distance=float(distance_entry.get())
                    time = float(time_entry.get())
                    if distance<0 or time<0:
                        messagebox.showerror(title="Error", message="Distance or time cannot be negative")
                    else:
                        speed=abs(distance/time)
                    result_label.config(text=f"{speed}")


                speed_label=tk.Label(speed_frame, text="Speed", bg="#212129",fg="#08edff",font=("Helvetica",34))
                distance_label=tk.Label(speed_frame,text="Distance",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                time_label=tk.Label(speed_frame,text="Time taken",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(speed_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))
                

                distance_entry=tk.Entry(speed_frame, font=("Helvetica", 16))
                time_entry=tk.Entry(speed_frame, font=("Helvetica", 16))

                speed_back=tk.Button(speed_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(speed_frame,phyf4c2_frame,result_label))
                speed_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(speed_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:speed_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                speed_label.grid(row=0,column=1,pady=10,padx=20)
                distance_label.grid(row=1,column=0,pady=10,padx=20)
                time_label.grid(row=2,column=0,pady=10,padx=50)

                distance_entry.grid(row=1,column=2,padx=20)
                time_entry.grid(row=2,column=2,padx=20)
                result_label.grid(row=3,column=1,pady=10)

            def velocity():
                backbutton(phyf4c2_frame,velocity_frame)
                def velocity_calc():
                    displacement=float(displacement_entry.get())
                    time = float(time_entry.get())
                    if time<0:
                        messagebox.showerror(title="Error", message="Time cannot be negative")
                    if time>0:
                        velocity=displacement/time
                    result_label.config(text=f"{velocity}")


                velocity_label=tk.Label(velocity_frame, text="Velocity", bg="#212129",fg="#08edff",font=("Helvetica",34))
                displacement_label=tk.Label(velocity_frame,text="Displacement",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                time_label=tk.Label(velocity_frame,text="Time taken",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(velocity_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                displacement_entry=tk.Entry(velocity_frame, font=("Helvetica", 16))
                time_entry=tk.Entry(velocity_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(velocity_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(velocity_frame,phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(velocity_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:velocity_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                velocity_label.grid(row=0,column=1,pady=20,padx=20)
                displacement_label.grid(row=1,column=0,pady=20,padx=40)
                time_label.grid(row=2,column=0,pady=20,padx=20)

                displacement_entry.grid(row=1,column=2,padx=20)
                time_entry.grid(row=2,column=2,padx=20)
                result_label.grid(row=3,column=1,pady=10)
            
            def acceleration():
                backbutton(phyf4c2_frame,acceleration_frame)
                def acceleration_calc():
                    v=float(fin_vel_entry.get())
                    u=float(ini_vel_entry.get())
                    t = float(time_entry.get())
                    if t<0:
                        messagebox.showerror(title="Error", message="Time cannot be negative")
                    if t>0:
                        acceleration=(v-u)/t
                    result_label.config(text=f"{acceleration}")


                acceleration_label=tk.Label(acceleration_frame, text="Acceleration", bg="#212129",fg="#08edff",font=("Helvetica",34))
                ini_vel_label=tk.Label(acceleration_frame,text="Initial Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                fin_vel_label=tk.Label(acceleration_frame,text="Final Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                time_label=tk.Label(acceleration_frame,text="Time taken",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(acceleration_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                ini_vel_entry=tk.Entry(acceleration_frame, font=("Helvetica", 16))
                fin_vel_entry=tk.Entry(acceleration_frame, font=("Helvetica", 16))
                time_entry=tk.Entry(acceleration_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(acceleration_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(acceleration_frame,phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(acceleration_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:acceleration_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                acceleration_label.grid(row=0,column=1,pady=10,padx=20)
                ini_vel_label.grid(row=1,column=0,pady=10,padx=20)
                fin_vel_label.grid(row=2,column=0,pady=10,padx=40)
                time_label.grid(row=3,column=0,pady=10,padx=20)

                ini_vel_entry.grid(row=1,column=2,padx=20)
                fin_vel_entry.grid(row=2,column=2,padx=20)
                time_entry.grid(row=3,column=2,padx=20)
                result_label.grid(row=4,column=1,pady=10)

            def momentum():
                backbutton(phyf4c2_frame,momentum_frame)
                def momentum_calc():
                    v=float(vel_entry.get())
                    m=float(mass_entry.get())
                    if m<0:
                        messagebox.showerror(title="Error", message="Mass cannot be negative")
                    else:
                        momentum=m*v
                    result_label.config(text=f"{momentum}")


                momentum_label=tk.Label(momentum_frame, text="Momentum", bg="#212129",fg="#08edff",font=("Helvetica",34))
                vel_label=tk.Label(momentum_frame,text="Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                mass_label=tk.Label(momentum_frame,text="Mass",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(momentum_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                vel_entry=tk.Entry(momentum_frame, font=("Helvetica", 16))
                mass_entry=tk.Entry(momentum_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(momentum_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(momentum_frame,phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(momentum_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:momentum_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                momentum_label.grid(row=0,column=1,pady=10,padx=20)
                vel_label.grid(row=1,column=0,pady=10,padx=70)
                mass_label.grid(row=2,column=0,pady=10,padx=20)

                vel_entry.grid(row=1,column=2,padx=20)
                mass_entry.grid(row=2,column=2,padx=20)
                result_label.grid(row=3,column=1,pady=10)

            def force():
                backbutton(phyf4c2_frame,force_frame)
                def force_calc():
                    m=float(mass_entry.get())
                    a=float(acc_entry.get())
                    if m<0:
                        messagebox.showerror(title="Error", message="Mass cannot be negative")
                    else:
                        force=m*a
                    result_label.config(text=f"{force}")


                force_label=tk.Label(force_frame, text="Force", bg="#212129",fg="#08edff",font=("Helvetica",34))
                mass_label=tk.Label(force_frame,text="Mass",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                acc_label=tk.Label(force_frame,text="Acceleration",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(force_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                mass_entry=tk.Entry(force_frame, font=("Helvetica", 16))
                acc_entry=tk.Entry(force_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(force_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(force_frame,phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(force_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:force_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                force_label.grid(row=0,column=1,pady=10,padx=20)
                mass_label.grid(row=1,column=0,pady=10,padx=20)
                acc_label.grid(row=2,column=0,pady=10,padx=50)

                mass_entry.grid(row=1,column=2,padx=20)
                acc_entry.grid(row=2,column=2,padx=20)
                result_label.grid(row=3,column=1,pady=10)

            def impulse():
                backbutton(phyf4c2_frame,impulse_frame)
                def impulse_calc():
                    m=float(mass_entry.get())
                    v=float(fin_vel_entry.get())
                    u=float(ini_vel_entry.get())
                    if m<0:
                        messagebox.showerror(title="Error", message="Mass cannot be negative")
                    else:
                        impulse=m*v-m*u
                    result_label.config(text=f"{impulse}")


                impulse_label=tk.Label(impulse_frame, text="Impulse", bg="#212129",fg="#08edff",font=("Helvetica",34))
                fin_vel_label=tk.Label(impulse_frame,text="Final Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                ini_vel_label=tk.Label(impulse_frame,text="Initial Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                mass_label=tk.Label(impulse_frame,text="Mass",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(impulse_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                fin_vel_entry=tk.Entry(impulse_frame, font=("Helvetica", 16))
                ini_vel_entry=tk.Entry(impulse_frame, font=("Helvetica", 16))
                mass_entry=tk.Entry(impulse_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(impulse_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(impulse_frame,phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(impulse_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:impulse_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                impulse_label.grid(row=0,column=1,pady=10,padx=20)
                fin_vel_label.grid(row=1,column=0,pady=10,padx=20)
                ini_vel_label.grid(row=2,column=0,pady=10,padx=40)
                mass_label.grid(row=3,column=0,pady=10,padx=20)

                fin_vel_entry.grid(row=1,column=2,padx=20)
                ini_vel_entry.grid(row=2,column=2,padx=20)
                mass_entry.grid(row=3,column=2,padx=20)
                result_label.grid(row=4,column=1,pady=10)

            def impulsiveForce():
                backbutton(phyf4c2_frame,impulsiveForce_frame)
                def impulsiveForce_calc():
                    m=float(mass_entry.get())
                    v=float(fin_vel_entry.get())
                    u=float(ini_vel_entry.get())
                    t=float(time_entry.get())
                    if m<0 or t<0:
                        messagebox.showerror(title="Error", message="Mass or time cannot be negative")
                    else:
                        impulsiveForce=(m*v-m*u)/t
                    result_label.config(text=f"{impulsiveForce}")


                impulsiveForce_label=tk.Label(impulsiveForce_frame, text="Impulsive Force", bg="#212129",fg="#08edff",font=("Helvetica",34))
                fin_vel_label=tk.Label(impulsiveForce_frame,text="Final Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                ini_vel_label=tk.Label(impulsiveForce_frame,text="Initial Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                mass_label=tk.Label(impulsiveForce_frame,text="Mass",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                time_label=tk.Label(impulsiveForce_frame,text="Time",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(impulsiveForce_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                fin_vel_entry=tk.Entry(impulsiveForce_frame, font=("Helvetica", 16))
                ini_vel_entry=tk.Entry(impulsiveForce_frame, font=("Helvetica", 16))
                mass_entry=tk.Entry(impulsiveForce_frame, font=("Helvetica", 16))
                time_entry=tk.Entry(impulsiveForce_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(impulsiveForce_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(impulsiveForce_frame,phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(impulsiveForce_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:impulsiveForce_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                impulsiveForce_label.grid(row=0,column=1,pady=10,padx=20)
                fin_vel_label.grid(row=1,column=0,pady=10,padx=50)
                ini_vel_label.grid(row=2,column=0,pady=10,padx=20)
                mass_label.grid(row=3,column=0,pady=10,padx=20)
                time_label.grid(row=4,column=0,pady=10,padx=20)

                fin_vel_entry.grid(row=1,column=2,padx=20)
                ini_vel_entry.grid(row=2,column=2,padx=20)
                mass_entry.grid(row=3,column=2,padx=20)
                time_entry.grid(row=4,column=2,padx=20)
                result_label.grid(row=5,column=1,pady=10)

            def weight():
                backbutton(phyf4c2_frame,weight_frame)
                def weight_calc():
                    m=float(mass_entry.get())
                    if m<0:
                        messagebox.showerror(title="Error", message="Mass cannot be negative")
                    else:
                        weight=m*9.81
                    result_label.config(text=f"{weight}")


                weight_label=tk.Label(weight_frame, text="Weight", bg="#212129",fg="#08edff",font=("Helvetica",34))
                mass_label=tk.Label(weight_frame,text="Mass",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(weight_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                mass_entry=tk.Entry(weight_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(weight_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(weight_frame,phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(weight_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:weight_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                weight_label.grid(row=0,column=1,pady=10,padx=20)
                mass_label.grid(row=1,column=0,pady=10,padx=100)

                mass_entry.grid(row=1,column=2,padx=20)
                result_label.grid(row=2,column=1,pady=10)
            
            f4Chapter2_label=tk.Label(phyf4c2_frame, text="Physics Form 4 Chapter 2", bg="#212129",fg="#08edff",font=("Helvetica",34))
            speed_button=tk.Button(phyf4c2_frame,text="Speed",bg="#90ee90", font=("Helvetica",24),command=lambda:speed())
            velocity_button=tk.Button(phyf4c2_frame,text="Velocity",bg="#90ee90", font=("Helvetica",24),command=lambda:velocity())
            acceleration_button=tk.Button(phyf4c2_frame,text="Acceleration",bg="#90ee90", font=("Helvetica",24),command=lambda:acceleration())
            momentum_button=tk.Button(phyf4c2_frame,text="Momentum",bg="#90ee90", font=("Helvetica",24),command=lambda:momentum())
            force_button=tk.Button(phyf4c2_frame,text="Force",bg="#90ee90", font=("Helvetica",24),command=lambda:force())
            impulse_button=tk.Button(phyf4c2_frame,text="Impulse",bg="#90ee90", font=("Helvetica",24),command=lambda:impulse())
            impulsive_force_button=tk.Button(phyf4c2_frame,text="Impulsive Force",bg="#90ee90", font=("Helvetica",24),command=lambda:impulsiveForce())
            weight_button=tk.Button(phyf4c2_frame,text="Weight",bg="#90ee90", font=("Helvetica",24),command=lambda:weight())

            phy_f4c2_back=tk.Button(phyf4c2_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(phyf4c2_frame,phyf4_frame))
            phy_f4c2_back.grid(row=9,column=1,pady=10)


            f4Chapter2_label.grid(row=0,column=1,padx=20,pady=10)
            speed_button.grid(row=1,column=1,pady=10,sticky="ew",padx=20)          
            velocity_button.grid(row=2,column=1,pady=10,sticky="ew",padx=20)          
            acceleration_button.grid(row=3,column=1,pady=10,sticky="ew",padx=20)       
            momentum_button.grid(row=4,column=1,pady=10,sticky="ew",padx=20)      
            force_button.grid(row=5,column=1,pady=10,sticky="ew",padx=20)        
            impulse_button.grid(row=6,column=1,pady=10,sticky="ew",padx=20)       
            impulsive_force_button.grid(row=7,column=1,pady=10,sticky="ew",padx=20)    
            weight_button.grid(row=8,column=1,pady=10,sticky="ew",padx=20)              
            


        f4Chapter_label=tk.Label(phyf4_frame, text="Physics Form 4", bg="#212129",fg="#08edff",font=("Helvetica",34))
        chap2_button=tk.Button(phyf4_frame,text="Chapter 2",bg="#90ee90", font=("Helvetica",24),command=lambda:phy_f4_chap2())
        chap3_button=tk.Button(phyf4_frame,text="Chapter 3",bg="#adb0b4", font=("Helvetica",24))
        chap4_button=tk.Button(phyf4_frame,text="Chapter 4",bg="#adb0b4", font=("Helvetica",24))
        chap5_button=tk.Button(phyf4_frame,text="Chapter 5",bg="#adb0b4", font=("Helvetica",24))
        chap6_button=tk.Button(phyf4_frame,text="Chapter 6",bg="#adb0b4", font=("Helvetica",24))

        phy_f4_back=tk.Button(phyf4_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(phyf4_frame,pack_surface))
        phy_f4_back.grid(row=6,column=2,pady=40)

        f4Chapter_label.grid(row=0,column=2,padx=10,pady=10)
        chap2_button.grid(row=1,column=0,padx=20,pady=50)
        chap3_button.grid(row=1,column=2,padx=20)
        chap4_button.grid(row=1,column=4,padx=20)
        chap5_button.grid(row=2,column=1,padx=20,pady=50)
        chap6_button.grid(row=2,column=3,padx=20)

    form4_button=tk.Button(phy_frame,text="Form 4", bg="#90ee90", font=("Helvetica",24), command=lambda:phy_f4())
    form5_button=tk.Button(phy_frame,text="Form 5", bg="#adb0b4", font=("Helvetica",24))
    chooseForm_label=tk.Label(phy_frame,text="Choose which form:",bg="#212129",fg="#08edff", font=("Helvetica",34))

    phy_back = tk.Button(phy_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(pack_surface,forget_surface))

    form4_button.grid(row=1,column=0,padx=20,pady=100)
    form5_button.grid(row=1,column=2,padx=20)
    chooseForm_label.grid(row=0,column=1,sticky="ew",padx=10,pady=10)
    phy_back.grid(row=6,column=1,pady=40)

def ChemistryPage(forget_surface, pack_surface):
    backbutton(forget_surface, pack_surface)
    def chem_f4():
        backbutton(chem_frame,chemf4_frame)
        def chem_f4_chap2():
            backbutton(chemf4_frame,chemf4c2_frame)
            def nucleon_number():
                backbutton(chemf4c2_frame, nucleon_frame)
                def nucleon_calc():
                    number_of_protons=int(number_of_protons_entry.get())
                    number_of_neutrons=int(number_of_neutrons_entry.get())
                    if number_of_protons <0 or number_of_neutrons <0:
                        messagebox.showerror(title="Error", message="Number of protons and number of neutrons cannot be negative")
                    else:
                        nucleon=number_of_protons + number_of_neutrons
                    result_label.config(text=f"{nucleon}")


                nucleon_label=tk.Label(nucleon_frame, text="Nucleon Number", bg="#212129",fg="#08edff",font=("Helvetica",34))
                number_of_protons_label=tk.Label(nucleon_frame,text="Number of Protons",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                number_of_neutrons_label=tk.Label(nucleon_frame,text="Number of Neutrons",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(nucleon_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                number_of_protons_entry=tk.Entry(nucleon_frame, font=("Helvetica", 16))
                number_of_neutrons_entry=tk.Entry(nucleon_frame, font=("Helvetica", 16))

                nucleon_back=tk.Button(nucleon_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(nucleon_frame,chemf4c2_frame,result_label))
                nucleon_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(nucleon_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:nucleon_calc())
                calculate_button.grid(row=8,column=1,pady=10)

                nucleon_label.grid(row=0,column=1,pady=10,padx=20)
                number_of_protons_label.grid(row=1,column=0,pady=10,padx=20)
                number_of_neutrons_label.grid(row=2,column=0,pady=10,padx=50)

                number_of_protons_entry.grid(row=1,column=2,padx=20)
                number_of_neutrons_entry.grid(row=2,column=2,padx=20)
                result_label.grid(row=3,column=2,padx=20)

            f4Chapter2_label=tk.Label(chemf4c2_frame, text="Physics Form 4 Chapter 2", bg="#212129",fg="#08edff",font=("Helvetica",34))
            nucleon_number_button=tk.Button(chemf4c2_frame,text="Speed",bg="#90ee90", font=("Helvetica",24),command=lambda:nucleon_number())
            

            chem_f4c2_back=tk.Button(chemf4c2_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(chemf4c2_frame,chemf4_frame))
            chem_f4c2_back.grid(row=9,column=1,pady=10)


            f4Chapter2_label.grid(row=0,column=1,padx=20,pady=10)
            nucleon_number_button.grid(row=1,column=1,pady=10,sticky="ew",padx=20)          
                    

        f4Chapter_label=tk.Label(chemf4_frame, text="Physics Form 4", bg="#212129",fg="#08edff",font=("Helvetica",34))
        chap2_button=tk.Button(chemf4_frame,text="Chapter 2",bg="#90ee90", font=("Helvetica",24),command=lambda:chem_f4_chap2())
        chap3_button=tk.Button(chemf4_frame,text="Chapter 3",bg="#adb0b4", font=("Helvetica",24))
        chap4_button=tk.Button(chemf4_frame,text="Chapter 4",bg="#adb0b4", font=("Helvetica",24))
        chap5_button=tk.Button(chemf4_frame,text="Chapter 5",bg="#adb0b4", font=("Helvetica",24))
        chap6_button=tk.Button(chemf4_frame,text="Chapter 6",bg="#adb0b4", font=("Helvetica",24))

        chem_f4_back=tk.Button(chemf4_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(chemf4_frame,pack_surface))
        chem_f4_back.grid(row=6,column=2,pady=40)

        f4Chapter_label.grid(row=0,column=2,padx=10,pady=10)
        chap2_button.grid(row=1,column=0,padx=20,pady=50)
        chap3_button.grid(row=1,column=2,padx=20)
        chap4_button.grid(row=1,column=4,padx=20)
        chap5_button.grid(row=2,column=1,padx=20,pady=50)
        chap6_button.grid(row=2,column=3,padx=20)
    
    
    form4_button=tk.Button(chem_frame,text="Form 4", bg="#90ee90", font=("Helvetica",24), command=lambda:chem_f4())
    form5_button=tk.Button(chem_frame,text="Form 5", bg="#adb0b4", font=("Helvetica",24))
    chooseForm_label=tk.Label(chem_frame,text="Choose which form:",bg="#212129",fg="#08edff", font=("Helvetica",34))

    chem_back = tk.Button(chem_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(pack_surface,forget_surface))

    form4_button.grid(row=1,column=0,padx=20,pady=100)
    form5_button.grid(row=1,column=2,padx=20)
    chooseForm_label.grid(row=0,column=1,sticky="ew",padx=10,pady=10)
    chem_back.grid(row=6,column=1,pady=40)


def admin():
        #global cursor
        #global conn
        global addToTree
        #conn=sqlite3.connect("data.db")
        #cursor=conn.cursor()
        backbutton(admin_frame,adminInterface_frame)
        def fetchStudent():
            conn=sqlite3.connect("data.db")
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM Student_Data")
            students=cursor.fetchall()
            #conn.commit()
            conn.close()
            return students
        def insertStudent(username,password,form,className):
            conn=sqlite3.connect("data.db")
            cursor=conn.cursor()
            cursor.execute("INSERT INTO Student_Data (username,password,form,className) VALUES(?,?,?,?)",(username,password,form,className))
            conn.commit()
            conn.close()
        def deleteStudent(username):
            conn=sqlite3.connect("data.db")
            cursor=conn.cursor()
            cursor.execute("DELETE FROM Student_Data WHERE username = ?",(username,))
            conn.commit()
            conn.close()
        def updateStudent(new_user,new_password,new_form,new_className,current_user):
            conn=sqlite3.connect("data.db")
            cursor=conn.cursor()
            cursor.execute("UPDATE Student_Data SET username = ?, password = ?, form = ?, className = ? WHERE username=?", (new_user,new_password,new_form,new_className,current_user))
            conn.commit()
            conn.close()
        def usernameExists(username):
            conn=sqlite3.connect("data.db")
            cursor=conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM Student_Data WHERE username = ?", (username,))
            result = cursor.fetchone()
            conn.close()
            return result[0] > 0 #return username if more than 0
        
        def addToTree():
            students=fetchStudent()
            tree.delete(*tree.get_children()) #delete content in tree view before inserting in tree view to prevent multiple times
            for student in students:
                tree.insert("", END, values=student)

        def insert():
            username=user_entry.get()
            password=password_entry.get()
            form=form_entry.get()
            className=className_entry.get()
            if not (username and password and form and className): #means kosong
                messagebox.showerror(title="Error", message="Enter all fields")
            elif usernameExists(username):
                messagebox.showerror(title="Error", message="Username already exists")
            else:
                insertStudent(username,password,form,className)
                addToTree()
            
        def clear(*clicked): 
            if clicked:
                tree.selection_remove(tree.focus()) #utk clearkan hover
            user_entry.delete(0,END) #clear dkt entry box
            password_entry.delete(0,END) #end represent the postiions after the last character in the widget
            form_entry.delete(0,END) # means we delete from index 0 till end
            className_entry.delete(0,END)
        
        def display_data(event):
            selected_item = tree.focus()
            if selected_item: #means we are clicking on the row, if the condition is true we will get the value of row yg line under ni
                row=tree.item(selected_item)["values"]
                clear()
                user_entry.insert(0,row[0]) #means we insert the values of row dkt entry, row=[0] means the 1st column, so we insert value of 1st column into username entry
                password_entry.insert(0,row[1])
                form_entry.insert(0,row[2])
                className_entry.insert(0,row[3])
            else: #if we are not clicking on a row, we pass
                pass

        def delete():
            selected_item=tree.focus()
            if not selected_item:
                messagebox.showerror(title="Error", message="Choose a student to delete")
            else:
                username=tree.item(selected_item)["values"][0] #get username from selected row
                #username=user_entry.get()
                deleteStudent(username)
                addToTree() #so we can get the data from databse after deletion
                clear()
        
        def update():
            selected_item=tree.focus()
            if not selected_item:
                messagebox.showerror(title="Error", message="Choose a student to update")
            else:
                current_username = tree.item(selected_item)["values"][0] #get current username from selected row
                username=user_entry.get()
                password=password_entry.get()
                form=form_entry.get()
                className=className_entry.get()
                updateStudent(username,password,form,className,current_username)
                addToTree()
                clear()
    
        adminCmd_frame=tk.Frame(adminInterface_frame, bg="#212129")
        adminCmd_frame.grid(row=0,column=0,padx=20,pady=20)

        adminAdd_frame=tk.Frame(adminCmd_frame,bg="#212129")
        adminDisplay_frame=tk.Frame(adminCmd_frame,bg="#212129")
        adminButtons_frame=tk.Frame(adminCmd_frame,bg="#212129")
        
        title_label=tk.Label(adminCmd_frame, text="Student Database", bg="#212129",fg="#08edff", font=("Helvetica",34))
        adminAdd_frame.grid(row=1,column=0,sticky="news",padx=10)
        adminDisplay_frame.grid(row=1,column=1,sticky="news",padx=10,rowspan=2)
        adminButtons_frame.grid(row=2,column=0,sticky="ew",padx=10)
        title_label.grid(row=0,column=0,pady=40,sticky='news')

        #add
        user=tk.Label(adminAdd_frame,text="Username",bg="#212129",fg="#FFFFFF",font=("Helvetica",16))
        password=tk.Label(adminAdd_frame,text="Password",bg="#212129",fg="#FFFFFF",font=("Helvetica",16))
        form=tk.Label(adminAdd_frame,text="Form",bg="#212129",fg="#FFFFFF",font=("Helvetica",16))
        className=tk.Label(adminAdd_frame,text="Class Name",bg="#212129",fg="#FFFFFF",font=("Helvetica",16))
        
        add_button=tk.Button(adminButtons_frame,text="Add Student",bg="#fa6126",fg="#FFFFFF",font=("Helvetica",16), command=lambda:insert())

        user_entry=tk.Entry(adminAdd_frame,font=("Helvetica", 16))
        password_entry=tk.Entry(adminAdd_frame,font=("Helvetica", 16))
        form_entry=ttk.Combobox(adminAdd_frame,values=["4", "5"],font=("Helvetica", 16))
        className_entry=ttk.Combobox(adminAdd_frame,values=["Perdana", "Bestari", "Satria"],font=("Helvetica", 16))

        user.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        password.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        form.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        className.grid(row=3,column=0,padx=10,pady=10,sticky="w")
        add_button.grid(row=4,sticky="s",padx=10,pady=0) #button sini

        user_entry.grid(row=0,column=1,pady=10,sticky="e",padx=10)
        password_entry.grid(row=1,column=1,pady=10,sticky="e",padx=10)
        form_entry.grid(row=2,column=1,pady=10,sticky="e",padx=10)
        className_entry.grid(row=3,column=1,pady=10,sticky="e",padx=10)

        #buttons
        updateStudent_button=tk.Button(adminButtons_frame,text="Update Student",bg="#fa6126",fg="#FFFFFF",font=("Helvetica",16),command=lambda:update())
        deleteStudent_button=tk.Button(adminButtons_frame,text="Delete Student",bg="#b81836",fg="#FFFFFF",font=("Helvetica",16),command=lambda:delete())
        back_button=tk.Button(adminButtons_frame,text="Back",bg="#1c6cc0",fg="#FFFFFF",font=("Helvetica",16), command=lambda:backbutton(adminInterface_frame,admin_frame))
    
        add_button.grid(row=0,column=0,padx=10,pady=10)
        updateStudent_button.grid(row=0,column=1,padx=10,pady=10)
        deleteStudent_button.grid(row=0,column=2,padx=10,pady=10)

        back_button.grid(row=1,column=1,padx=10,pady=10)

        #display table
        tree=ttk.Treeview(adminDisplay_frame)
        tree["columns"]=("Username", "Password", "Form", "Class Name")
        tree.column("#0",width=0,stretch=tk.NO) # utk hide default first column
        tree.column("Username", anchor=tk.CENTER,width=120)
        tree.column("Password", anchor=tk.CENTER,width=120)
        tree.column("Form", anchor=tk.CENTER,width=120)
        tree.column("Class Name", anchor=tk.CENTER,width=120)

        tree.heading("Username", text="Username")
        tree.heading("Password", text="Password")
        tree.heading("Form", text="Form")
        tree.heading("Class Name", text="Class Name")

        tree.grid(row=0,column=0,sticky="news")
        clearSelection_button=tk.Button(adminDisplay_frame,text="Clear Selection",bg="#b81836",fg="#FFFFFF",font=("Helvetica",16), command=lambda:clear(True))
        clearSelection_button.grid(row=6,column=0,sticky="news")

        addToTree()
        tree.bind("<ButtonRelease>", display_data) #means if we click on a row in the tree view, the function will be executed

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
username_label.grid(row=1, column=0,padx=10)
username_entry.grid(row=1, column=1, pady=20,padx=10)
password_label.grid(row=2, column=0,padx=10)
password_entry.grid(row=2, column=1, pady=20,padx=10)
login_button.grid(row=3, column=0,columnspan=2,padx=20,pady=5,sticky="EW" )
register_button.grid(row=4,column=0,columnspan=2,padx=20,pady=5,sticky="EW" )



frame.place(relx=0.5, rely=0.5,anchor='center')

window.mainloop()

