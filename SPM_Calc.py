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
admin_frame=tk.Frame(bg="#212129")
adminInterface_frame=tk.Frame(bg="#212129")

#form 4 frames tkleh tgk form 5
f4_subject_frame=tk.Frame(bg="#212129")

f4_phy_frame=tk.Frame(bg="#212129")
f4_phyf4_frame=tk.Frame(bg="#212129")
f4_phyf4c2_frame=tk.Frame(bg="#212129")
f4_speed_frame=tk.Frame(bg="#212129")
f4_velocity_frame=tk.Frame(bg="#212129")
f4_acceleration_frame=tk.Frame(bg="#212129")
f4_momentum_frame=tk.Frame(bg="#212129")
f4_force_frame=tk.Frame(bg="#212129")
f4_impulse_frame=tk.Frame(bg="#212129")
f4_impulsiveForce_frame=tk.Frame(bg="#212129")
f4_weight_frame=tk.Frame(bg="#212129")

f4_chem_frame=tk.Frame(bg="#212129")
f4_chemf4_frame=tk.Frame(bg="#212129")
f4_chemf4c2_frame=tk.Frame(bg="#212129")
f4_nucleon_frame=tk.Frame(bg="#212129")

f4_bio_frame=tk.Frame(bg="#212129")
f4_biof4_frame=tk.Frame(bg="#212129")
f4_biof4c4_frame=tk.Frame(bg="#212129")
f4_biof4c5_frame=tk.Frame(bg="#212129")
f4_biof4c7_frame=tk.Frame(bg="#212129")
f4_percentage_diff_in_mass_frame=tk.Frame(bg="#212129")
f4_enzyme_reaction_rate_frame=tk.Frame(bg="#212129")
f4_energy_value_food_sample_frame=tk.Frame(bg="#212129")

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

phyf5_frame=tk.Frame(bg="#212129")
phyf5c1_frame=tk.Frame(bg="#212129")
hookesLaw_frame=tk.Frame(bg="#212129")
elasPotEn_frame=tk.Frame(bg="#212129")

phyf5c3_frame=tk.Frame(bg="#212129")

#chemistry
chem_frame=tk.Frame(bg="#212129")
chemf4_frame=tk.Frame(bg="#212129")
chemf4c2_frame=tk.Frame(bg="#212129")
nucleon_frame=tk.Frame(bg="#212129")

chemf5_frame=tk.Frame(bg="#212129")
chemf5c3_frame=tk.Frame(bg="#212129")
fuelValue_frame=tk.Frame(bg="#212129")
#biology
bio_frame=tk.Frame(bg="#212129")
biof4_frame=tk.Frame(bg="#212129")
biof4c4_frame=tk.Frame(bg="#212129")
biof4c5_frame=tk.Frame(bg="#212129")
biof4c7_frame=tk.Frame(bg="#212129")
biof5_frame=tk.Frame(bg="#212129")
biof5c9_frame=tk.Frame(bg="#212129")
percentage_diff_in_mass_frame=tk.Frame(bg="#212129")
enzyme_reaction_rate_frame=tk.Frame(bg="#212129")
energy_value_food_sample_frame=tk.Frame(bg="#212129")
percentage_cover_frame=tk.Frame(bg="#212129")
population_frame=tk.Frame(bg="#212129")
transpiration_rate_frame=tk.Frame(bg="#212129")

def register(): #function utk kalau click register keluar page register
    global frame
    global register_frame
    global form_combobox

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
        form=result[0][2]
        if result == []:
            messagebox.showerror(title="Error", message="Account not found")
        elif result !=[] and username!= "admin" and password!="admin" and form ==4: #means form 4
            backbutton(frame,f4_subject_frame)
            subject_label = tk.Label(f4_subject_frame, text="Choose a subject", bg="#212129",fg="#08edff", font=("Helvetica",34))

            phy_button = tk.Button(f4_subject_frame, text="Physics", bg="#90ee90", font=("Helvetica",24),command=lambda:f4_PhysicsPage(f4_subject_frame))
            chem_button = tk.Button(f4_subject_frame, text="Chemistry", bg="#add8e6", font=("Helvetica",24),command=lambda:f4_ChemistryPage(f4_subject_frame))
            bio_button = tk.Button(f4_subject_frame, text="Biology", bg="#f08080", font=("Helvetica",24),command=lambda:f4_BiologyPage(f4_subject_frame))

            subject_back = tk.Button(f4_subject_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(f4_subject_frame,frame))

            subject_label.grid(row=0,column=1,columnspan=2,sticky="news",padx=50,pady=40)
            subject_back.grid(row=6,column=1,columnspan=2,padx=20,pady=40)
            phy_button.grid(row=1,column=1,columnspan=2,padx=20,pady=20,sticky="ew")
            chem_button.grid(row=2,column=1,columnspan=2,padx=20,pady=20,sticky="ew")
            bio_button.grid(row=3,column=1,columnspan=2,padx=20,pady=20,sticky="ew")


        elif result !=[] and username!= "admin" and password!="admin" and form ==5:  #means form 5
            backbutton(frame,subject_frame)
            subject_label = tk.Label(subject_frame, text="Choose a subject", bg="#212129",fg="#08edff", font=("Helvetica",34))

            phy_button = tk.Button(subject_frame, text="Physics", bg="#90ee90", font=("Helvetica",24),command=lambda:PhysicsPage(subject_frame,phy_frame))
            chem_button = tk.Button(subject_frame, text="Chemistry", bg="#add8e6", font=("Helvetica",24),command=lambda:ChemistryPage(subject_frame,chem_frame))
            bio_button = tk.Button(subject_frame, text="Biology", bg="#f08080", font=("Helvetica",24),command=lambda:BiologyPage(subject_frame,bio_frame))

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
            bio_button = tk.Button(admin_frame, text="Biology", bg="#f08080", font=("Helvetica",24),command=lambda:ChemistryPage(admin_frame,bio_frame))
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
                    result_label.config(text=f"{speed} m/s")


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
                    result_label.config(text=f"{velocity} m/s")


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
                    result_label.config(text=f"{acceleration} m/s^2")


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
                    result_label.config(text=f"{momentum} kg m/s")


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
                    result_label.config(text=f"{force} N")


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
                    result_label.config(text=f"{impulse} N/s")


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
                    result_label.config(text=f"{impulsiveForce} N")


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
                    result_label.config(text=f"{weight} N")


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

    def phy_f5():
        backbutton(phy_frame,phyf5_frame)
        def phy_f5_chap1():
            backbutton(phyf5_frame,phyf5c1_frame)
            def hookesLaw():
                backbutton(phyf4c2_frame,hookesLaw_frame)
                def hookesLaw_calc():
                    k=float(springConstant_entry.get())
                    x=float(springExtension_entry.get())
                    if k<0:
                        messagebox.showerror(title="Error", message="Spring constant cannot be negative")
                    else:
                        force=k*x
                    result_label.config(text=f"{force} N/m")


                hookesLaw_label=tk.Label(hookesLaw_frame, text="Force (Hookes' Law)", bg="#212129",fg="#08edff",font=("Helvetica",34))
                springConstant_label=tk.Label(hookesLaw_frame,text="Spring Constant",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                springExtension_label=tk.Label(hookesLaw_frame,text="Spring Extension",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(hookesLaw_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                springConstant_entry=tk.Entry(hookesLaw_frame, font=("Helvetica", 16))
                springExtension_entry=tk.Entry(hookesLaw_frame, font=("Helvetica", 16))

                hookesLaw_back=tk.Button(hookesLaw_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(hookesLaw_frame,phyf5c1_frame,result_label))
                hookesLaw_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(hookesLaw_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:hookesLaw_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                hookesLaw_label.grid(row=0,column=1,pady=10,padx=20)
                springConstant_label.grid(row=1,column=0,pady=10,padx=20)
                springExtension_label.grid(row=2,column=0,pady=10,padx=50)

                springConstant_entry.grid(row=1,column=2,padx=20)
                springExtension_entry.grid(row=2,column=2,padx=50)
                result_label.grid(row=3,column=1,pady=10)

            def elasPotEn():
                backbutton(phyf4c2_frame,elasPotEn_frame)
                def elasPotEn_calc():
                    k=float(springConstant_entry.get())
                    x=float(springExtension_entry.get())
                    if k<0:
                        messagebox.showerror(title="Error", message="Spring constant cannot be negative")
                    else:
                        energy=(1/2)*k*(x**2)
                    result_label.config(text=f"{energy} J")


                elasPotEn_label=tk.Label(elasPotEn_frame, text="Elastic Potential Energy", bg="#212129",fg="#08edff",font=("Helvetica",34))
                springConstant_label=tk.Label(elasPotEn_frame,text="Spring Constant",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                springExtension_label=tk.Label(elasPotEn_frame,text="Spring Extension",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(elasPotEn_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                springConstant_entry=tk.Entry(elasPotEn_frame, font=("Helvetica", 16))
                springExtension_entry=tk.Entry(elasPotEn_frame, font=("Helvetica", 16))

                elasPotEn_back=tk.Button(elasPotEn_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(elasPotEn_frame,phyf5c1_frame,result_label))
                elasPotEn_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(elasPotEn_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:elasPotEn_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                elasPotEn_label.grid(row=0,column=1,pady=10,padx=20)
                springConstant_label.grid(row=1,column=0,pady=10,padx=20)
                springExtension_label.grid(row=2,column=0,pady=10,padx=50)

                springConstant_entry.grid(row=1,column=2,padx=20)
                springExtension_entry.grid(row=2,column=2,padx=50)
                result_label.grid(row=3,column=1,pady=10)

            f5Chapter1_label=tk.Label(phyf5c1_frame, text="Physics Form 5 Chapter 1", bg="#212129",fg="#08edff",font=("Helvetica",34))
            hookesLaw_button=tk.Button(phyf5c1_frame,text="Force (Hooke's Law)",bg="#90ee90", font=("Helvetica",24),command=lambda:hookesLaw())
            elasPotEn_button=tk.Button(phyf5c1_frame,text="Elastic Potential Energy",bg="#90ee90", font=("Helvetica",24),command=lambda:elasPotEn())

            phy_f5c1_back=tk.Button(phyf5c1_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(phyf5c1_frame,phyf5_frame))
            phy_f5c1_back.grid(row=9,column=1,pady=10)

            f5Chapter1_label.grid(row=0,column=1,padx=20,pady=10)
            hookesLaw_button.grid(row=1,column=1,pady=10,sticky="ew",padx=20)          
            elasPotEn_button.grid(row=2,column=1,pady=10,sticky="ew",padx=20) 

        def phy_f5_chap3():
            backbutton(phyf5_frame,phyf5c3_frame)
            def weight():
                backbutton(phyf5c3_frame,weight_frame)
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

                weight_back=tk.Button(weight_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(weight_frame,phyf5c3_frame,result_label))
                weight_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(weight_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:weight_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                weight_label.grid(row=0,column=1,pady=10)
                mass_label.grid(row=1,column=0,pady=10)

                mass_entry.grid(row=1,column=2)
                result_label.grid(row=2,column=1,pady=10)
            f5Chapter3_label=tk.Label(phyf4c2_frame, text="Physics Form 5 Chapter 3", bg="#212129",fg="#08edff",font=("Helvetica",34))
            f5Chapter3_label.grid(row=0,column=1,pady=10)
            weight_button=tk.Button(phyf5c3_frame,text="weight",bg="#90ee90", font=("Helvetica",24),command=lambda:weight())
            weight_button.grid(row=1,column=1,pady=10,sticky="ew")   
            backbutton_weight_c3 = tk.Button(phyf5c3_frame, text='Back',  bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda: backbutton(phyf5c3_frame, phyf5_frame)) 
            backbutton_weight_c3.grid(row=6,column=1)

            f5Chapter3_label=tk.Label(phyf5c3_frame, text="Physics Form 5 Chapter 3", bg="#212129",fg="#08edff",font=("Helvetica",34))
            f5Chapter3_label.grid(row=0,column=1,pady=10)

        f5Chapter_label=tk.Label(phyf5_frame, text="Physics Form 5", bg="#212129",fg="#08edff",font=("Helvetica",34))
        chap1_button=tk.Button(phyf5_frame,text="Chapter 1",bg="#90ee90", font=("Helvetica",24),command=lambda:phy_f5_chap1())
        chap2_button=tk.Button(phyf5_frame,text="Chapter 2",bg="#adb0b4", font=("Helvetica",24))
        chap3_button=tk.Button(phyf5_frame,text="Chapter 3",bg="#90ee90", font=("Helvetica",24),command=lambda:phy_f5_chap3())
        chap4_button=tk.Button(phyf5_frame,text="Chapter 4",bg="#adb0b4", font=("Helvetica",24))
        chap5_button=tk.Button(phyf5_frame,text="Chapter 5",bg="#adb0b4", font=("Helvetica",24))
        chap6_button=tk.Button(phyf5_frame,text="Chapter 6",bg="#adb0b4", font=("Helvetica",24))
        chap7_button=tk.Button(phyf5_frame,text="Chapter 7",bg="#adb0b4", font=("Helvetica",24))

        chem_f4_back=tk.Button(phyf5_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(phyf5_frame,pack_surface))
        chem_f4_back.grid(row=6,column=2,pady=40)

        f5Chapter_label.grid(row=0,column=2,padx=10,pady=10)
        chap1_button.grid(row=1,column=0,padx=20,pady=50)
        chap2_button.grid(row=1,column=2,padx=20)
        chap3_button.grid(row=1,column=4,padx=20)
        chap4_button.grid(row=2,column=0,padx=20,pady=50)
        chap5_button.grid(row=2,column=2,padx=20)
        chap6_button.grid(row=2,column=4,padx=20)
        chap7_button.grid(row=3,column=2,padx=20,pady=50)

    form4_button=tk.Button(phy_frame,text="Form 4", bg="#90ee90", font=("Helvetica",24), command=lambda:phy_f4())
    form5_button=tk.Button(phy_frame,text="Form 5", bg="#90ee90", font=("Helvetica",24), command=lambda:phy_f5())
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
                number_of_protons_label.grid(row=1,column=0,pady=10,padx=10)
                number_of_neutrons_label.grid(row=2,column=0,pady=10,padx=10)

                number_of_protons_entry.grid(row=1,column=2,padx=20)
                number_of_neutrons_entry.grid(row=2,column=2,padx=20)
                result_label.grid(row=3,column=1,padx=20)

            f4Chapter2_label=tk.Label(chemf4c2_frame, text="Chemistry Form 4 Chapter 2", bg="#212129",fg="#08edff",font=("Helvetica",34))
            nucleon_number_button=tk.Button(chemf4c2_frame,text="Nucleon Number",bg="#add8e6", font=("Helvetica",24),command=lambda:nucleon_number())
            

            chem_f4c2_back=tk.Button(chemf4c2_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(chemf4c2_frame,chemf4_frame))
            chem_f4c2_back.grid(row=9,column=1,pady=10)


            f4Chapter2_label.grid(row=0,column=1,padx=20,pady=10)
            nucleon_number_button.grid(row=1,column=1,pady=10,sticky="ew",padx=20)          
                    

        f4Chapter_label=tk.Label(chemf4_frame, text="Chemistry Form 4", bg="#212129",fg="#08edff",font=("Helvetica",34))
        chap2_button=tk.Button(chemf4_frame,text="Chapter 2",bg="#add8e6", font=("Helvetica",24),command=lambda:chem_f4_chap2())
        chap3_button=tk.Button(chemf4_frame,text="Chapter 3",bg="#adb0b4", font=("Helvetica",24))
        chap4_button=tk.Button(chemf4_frame,text="Chapter 4",bg="#adb0b4", font=("Helvetica",24))
        chap5_button=tk.Button(chemf4_frame,text="Chapter 5",bg="#adb0b4", font=("Helvetica",24))
        chap6_button=tk.Button(chemf4_frame,text="Chapter 6",bg="#adb0b4", font=("Helvetica",24))
        chap7_button=tk.Button(chemf4_frame,text="Chapter 7",bg="#adb0b4", font=("Helvetica",24))
        chap8_button=tk.Button(chemf4_frame,text="Chapter 8",bg="#adb0b4", font=("Helvetica",24))
        

        chem_f4_back=tk.Button(chemf4_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(chemf4_frame,pack_surface))
        chem_f4_back.grid(row=6,column=2,pady=40)

        f4Chapter_label.grid(row=0,column=2,padx=10,pady=10)
        chap2_button.grid(row=1,column=0,padx=20,pady=50)
        chap3_button.grid(row=1,column=2,padx=20)
        chap4_button.grid(row=1,column=4,padx=20)
        chap5_button.grid(row=2,column=0,padx=20,pady=50)
        chap6_button.grid(row=2,column=2,padx=20)
        chap7_button.grid(row=2,column=4,padx=20)
        chap8_button.grid(row=3,column=2,padx=20,pady=50)
    
    def chem_f5():
        backbutton(chem_frame,chemf5_frame)
        def chem_f5_chap3():
            backbutton(chemf5_frame,chemf5c3_frame)
            def fuelValue():
                backbutton(chemf5c3_frame, fuelValue_frame)
                def fuelValue_calc():
                    heat=float(heat_entry.get())
                    molMass=float(molMass_entry.get())
                    if molMass <0:
                        messagebox.showerror(title="Error", message="Molar Mass cannot be negative")
                    else:
                        fuelValue=heat/molMass
                    result_label.config(text=f"{fuelValue} kJ/g")

                fuelValue_label=tk.Label(fuelValue_frame, text="Fuel Value", bg="#212129",fg="#08edff",font=("Helvetica",34))
                heat_label=tk.Label(fuelValue_frame,text="Heat of Combustion",bg="#212129",fg="#add8e6", font=("Helvetica", 24))
                molMass_label=tk.Label(fuelValue_frame,text="Molar Mass",bg="#212129",fg="#add8e6", font=("Helvetica", 24))
                result_label=tk.Label(fuelValue_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                heat_entry=tk.Entry(fuelValue_frame, font=("Helvetica", 16))
                molMass_entry=tk.Entry(fuelValue_frame, font=("Helvetica", 16))

                nucleon_back=tk.Button(fuelValue_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(fuelValue_frame,chemf5c3_frame,result_label))
                nucleon_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(fuelValue_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:fuelValue_calc())
                calculate_button.grid(row=8,column=1,pady=10)

                fuelValue_label.grid(row=0,column=1,pady=10,padx=20)
                heat_label.grid(row=1,column=0,pady=10,padx=10)
                molMass_label.grid(row=2,column=0,pady=10,padx=10)

                heat_entry.grid(row=1,column=2,padx=20)
                molMass_entry.grid(row=2,column=2,padx=20)
                result_label.grid(row=3,column=1,padx=20)

            f5Chapter3_label=tk.Label(chemf5c3_frame, text="Chemistry Form 5 Chapter 3", bg="#212129",fg="#08edff",font=("Helvetica",34))
            fuelValue_button=tk.Button(chemf5c3_frame,text="Fuel Value",bg="#add8e6", font=("Helvetica",24),command=lambda:fuelValue())
            

            chem_f4c2_back=tk.Button(chemf5c3_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(chemf5c3_frame,chemf5_frame))
            chem_f4c2_back.grid(row=9,column=1,pady=10)


            f5Chapter3_label.grid(row=0,column=1,padx=20,pady=10)
            fuelValue_button.grid(row=1,column=1,pady=10,sticky="ew",padx=20)          

        chem_f5_back=tk.Button(chemf5_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(chemf5_frame,pack_surface))
        chem_f5_back.grid(row=6,column=2,pady=40)

        f5Chapter_label=tk.Label(chemf5_frame, text="Chemistry Form 5", bg="#212129",fg="#08edff",font=("Helvetica",34))
        chap3_button=tk.Button(chemf5_frame,text="Chapter 3",bg="#add8e6", font=("Helvetica",24),command=lambda:chem_f5_chap3())

        f5Chapter_label.grid(row=0,column=2,padx=10,pady=10)
        chap3_button.grid(row=1,column=2,padx=20,pady=50)

    form4_button=tk.Button(chem_frame,text="Form 4", bg="#add8e6", font=("Helvetica",24), command=lambda:chem_f4())
    form5_button=tk.Button(chem_frame,text="Form 5", bg="#add8e6", font=("Helvetica",24), command=lambda:chem_f5())
    chooseForm_label=tk.Label(chem_frame,text="Choose which form:",bg="#212129",fg="#08edff", font=("Helvetica",34))

    chem_back = tk.Button(chem_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(pack_surface,forget_surface))

    form4_button.grid(row=1,column=0,padx=20,pady=100)
    form5_button.grid(row=1,column=2,padx=20)
    chooseForm_label.grid(row=0,column=1,sticky="ew",padx=10,pady=10)
    chem_back.grid(row=6,column=1,pady=40)

def BiologyPage(forget_surface,pack_surface):
    backbutton(forget_surface,pack_surface)
    def bio_f4():
        backbutton(bio_frame,biof4_frame)
        def bio_f4_chap4():
            backbutton(biof4_frame,biof4c4_frame)

            form_4_chapter_4_label=tk.Label(biof4c4_frame, text='Biology form 4 chapter 2 ', bg="#212129",fg="#08edff",font=("Helvetica",34))
            form_4_chapter_4_label.grid(row=0,column=1,pady=10,padx=20)
            percentage_diff_in_mass_button=tk.Button(biof4c4_frame, text='Percentage difference in mass', bg="#f08080", font=("Helvetica",24), command=lambda:percentage_diff_in_mass())
            percentage_diff_in_mass_button.grid(row=1,column=1,pady=10,padx=20,sticky="ew")
            backbutton_f4c4=tk.Button(biof4c4_frame, text='Back', bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16) ,command=lambda:backbutton(biof4c4_frame,biof4_frame) )
            backbutton_f4c4.grid(row=9,column=1,pady=10)

            def percentage_diff_in_mass():
                backbutton(biof4c4_frame, percentage_diff_in_mass_frame)
                def percentage_difference_in_mass_calc():
                    final_mass = int(final_mass_entry.get())
                    initial_mass = int(initial_mass_entry.get())
                    if final_mass<0 or initial_mass<0:
                        messagebox.showerror(title="Error", message="final or initial mass cannot be negative")
                    else:
                            percentage_difference_in_mass = ((final_mass-initial_mass)/initial_mass)*0.01
                    result_label.config(text=f"{percentage_difference_in_mass} %")
                
                percentage_diff_in_mass_label = tk.Label(percentage_diff_in_mass_frame, text="Percentage Difference in Mass",bg="#212129",fg="#08edff",font=("Helvetica",34))
                final_mass_label= tk.Label(percentage_diff_in_mass_frame,text="Final mass",bg="#212129",fg="#f08080", font=("Helvetica", 24))
                initial_mass_label = tk.Label(percentage_diff_in_mass_frame,text="Initial mass",bg="#212129",fg="#f08080", font=("Helvetica", 24)) 
                result_label = tk.Label(percentage_diff_in_mass_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))
                final_mass_entry = tk.Entry(percentage_diff_in_mass_frame, font=("Helvetica", 16))
                initial_mass_entry = tk.Entry(percentage_diff_in_mass_frame, font=("Helvetica", 16))
                percentage_diff_in_mass_back = tk.Button(percentage_diff_in_mass_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(percentage_diff_in_mass_frame,biof4c4_frame,result_label))
                percentage_diff_in_mass_back.grid(row=9,column=1,pady=10)
                calculate_button = tk.Button(percentage_diff_in_mass_frame, text='Calculate',bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:percentage_difference_in_mass_calc())
                calculate_button.grid(row=8,column=1,pady=10)
                percentage_diff_in_mass_label.grid(row=0, column=1,pady=10)
                final_mass_label.grid(row=1,column=0, pady=10,padx=20)
                initial_mass_label.grid(row=2, column=0,pady=10,padx=20)
                final_mass_entry.grid(row=1,column=2,padx=20)
                initial_mass_entry.grid(row=2, column=2,padx=20)
                result_label.grid(row=3,column=1,pady=10,padx=20)

        def bio_f4_chap5():
            backbutton(biof4_frame,biof4c5_frame)

            form_4_chapter_5_label=tk.Label(biof4c5_frame,text='Biology Form 4 Chapter 5' ,bg="#212129",fg="#08edff",font=("Helvetica",34))
            form_4_chapter_5_label.grid(row=0,column=1,pady=10,padx=20)
            enzyme_reaction_rate_button=tk.Button(biof4c5_frame,text='Enzyme Reaction Rate', bg="#f08080", font=("Helvetica",24),command=lambda:enzyme_reaction_rate())
            enzyme_reaction_rate_button.grid(row=1,column=1,pady=10,padx=20,sticky="ew")
            backbutton_f4c5=tk.Button(biof4c5_frame, text='Back' , bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:backbutton(biof4c5_frame,biof4_frame))
            backbutton_f4c5.grid(row=9,column=1,pady=10)

            def enzyme_reaction_rate():
                backbutton(biof4c5_frame, enzyme_reaction_rate_frame)
                def enzyme_reaction_rate_calc():
                    time_taken=int(time_entry.get())    
                    if time_taken<0:
                        messagebox.showerror(title="Error", message="time cannot be negative")
                    else:
                         enzyme_reaction_rate = 1/time_taken
                    rounded_rate=round(enzyme_reaction_rate,4)
                    result_label.config(text=f"{rounded_rate} s") 
                enzyme_reaction_rate_label=tk.Label(enzyme_reaction_rate_frame, text='Enzyme Reaction Rate',bg="#212129",fg="#08edff",font=("Helvetica",34) )    
                time_label=tk.Label(enzyme_reaction_rate_frame,text='Time',bg="#212129",fg="#f08080",font=("Helvetica",34))
                result_label=tk.Label(enzyme_reaction_rate_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))
                time_entry=tk.Entry(enzyme_reaction_rate_frame, font=("Helvetica", 16))
                enzyme_reaction_rate_back=tk.Button(enzyme_reaction_rate_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(enzyme_reaction_rate_frame,biof4c5_frame,result_label))
                enzyme_reaction_rate_back.grid(row=9, column=1, pady=10)
                calculate_button=tk.Button(enzyme_reaction_rate_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:enzyme_reaction_rate_calc())
                calculate_button.grid(row=8,column=1,pady=10)
                enzyme_reaction_rate_label.grid(row=0,column=1,pady=10)
                time_label.grid(row=1,column=0,pady=10,padx=70)
                time_entry.grid(row=1,column=2,padx=20)
                result_label.grid(row=3,column=1,pady=10,padx=20)
        def bio_f4_chap7():
            backbutton(biof4_frame, biof4c7_frame)

            form_4_chapter_7_label = tk.Label(biof4c7_frame, text='Biology Form 4 Chapter 7', bg="#212129",fg="#08edff",font=("Helvetica",34))
            form_4_chapter_7_label.grid(row=0,column=1,pady=10,padx=20)

            energy_value_food_sample_button = tk.Button(biof4c7_frame, text='Energy Value Food Sample', bg="#f08080", font=("Helvetica",24), command=lambda: energy_value_food_sample())
            energy_value_food_sample_button.grid(row=1,column=1,pady=10,sticky="ew",padx=20)

            backbutton_f4c7 = tk.Button(biof4c7_frame, text='Back',  bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda: backbutton(biof4c7_frame, biof4_frame))
            backbutton_f4c7.grid(row=9,column=1,pady=10,padx=20)

            def energy_value_food_sample():
                backbutton(biof4c7_frame, energy_value_food_sample_frame)
                def energy_value_food_sample_calc():
                    try:
                        mass_water = int(mass_water_entry.get())
                        temperature_rise = int(temperature_rise_entry.get())
                        mass_food = int(mass_food_entry.get())
                        if mass_food < 0 or mass_water < 0 or temperature_rise < 0:
                            messagebox.showerror(title='Error', message="Mass of water, food, and temperature rise cannot be negative")
                        else:
                            energy_value_food_sample = (4.2 * mass_water * temperature_rise) / mass_food * 1000
                            result_label.config(text=f"Energy Value: {energy_value_food_sample:.2f} J/g")
                    except ValueError:
                        messagebox.showerror(title='Error', message="Please enter valid numbers")
                energy_value_food_sample_label = tk.Label(energy_value_food_sample_frame, text='Energy Value Food Sample', bg="#212129", fg="#08edff", font=("Helvetica", 34))
                energy_value_food_sample_label.grid(row=0, column=1, pady=10)
                mass_water_label = tk.Label(energy_value_food_sample_frame, text='Mass Water (g)', bg="#212129", fg="#f08080", font=("Helvetica", 24))
                mass_water_label.grid(row=1, column=0, pady=10)
                mass_water_entry = tk.Entry(energy_value_food_sample_frame, font=("Helvetica", 16))
                mass_water_entry.grid(row=1, column=2, pady=10)
                temperature_rise_label = tk.Label(energy_value_food_sample_frame, text='Temperature Rise (°C)', bg="#212129", fg="#f08080", font=("Helvetica", 24))
                temperature_rise_label.grid(row=2, column=0, pady=10,padx=20)
                temperature_rise_entry = tk.Entry(energy_value_food_sample_frame, font=("Helvetica", 16))
                temperature_rise_entry.grid(row=2, column=2, pady=10)
                mass_food_label = tk.Label(energy_value_food_sample_frame, text='Mass Food (g)', bg="#212129", fg="#f08080", font=("Helvetica", 24))
                mass_food_label.grid(row=3, column=0, pady=10)
                mass_food_entry = tk.Entry(energy_value_food_sample_frame, font=("Helvetica", 16))
                mass_food_entry.grid(row=3, column=2, pady=10,padx=50)
                calculate_button = tk.Button(energy_value_food_sample_frame, text="Calculate", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=energy_value_food_sample_calc)
                calculate_button.grid(row=5, column=1, pady=10)
                result_label = tk.Label(energy_value_food_sample_frame, text='', bg="#212129", fg="#FFFFFF", font=("Helvetica", 24))
                result_label.grid(row=4, column=1, pady=10)
                energy_value_food_sample_back = tk.Button(energy_value_food_sample_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda: backbutton_delresult(energy_value_food_sample_frame, biof4c7_frame,result_label))
                energy_value_food_sample_back.grid(row=6, column=1, pady=10)
                
        f4Chapter_label=tk.Label(biof4_frame, text="Biology Form 4", bg="#212129",fg="#08edff",font=("Helvetica",34))
        chap4_button=tk.Button(biof4_frame,text="Chapter 4",bg="#f08080", font=("Helvetica",24),command=lambda:bio_f4_chap4())
        chap5_button=tk.Button(biof4_frame,text="Chapter 5",bg="#f08080", font=("Helvetica",24),command=lambda:bio_f4_chap5())
        chap7_button=tk.Button(biof4_frame,text="Chapter 7",bg="#f08080", font=("Helvetica",24),command=lambda:bio_f4_chap7())
        bio_f4_back=tk.Button(biof4_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(biof4_frame,pack_surface))
        bio_f4_back.grid(row=6,column=2,pady=10)
        
        f4Chapter_label.grid(row=0,column=2,padx=10,pady=10)  
        chap4_button.grid(row=1,column=0,padx=10,pady=50)
        chap5_button.grid(row=1,column=2,padx=10)
        chap7_button.grid(row=1,column=4,padx=10)
        
    def bio_f5():
        backbutton(bio_frame,biof5_frame)
        def bio_f5_chap9():
            backbutton(biof5_frame,biof5c9_frame)

            form_5_chapter_9_label = tk.Label(biof5c9_frame, text='Biology Form 5 Chapter 9',bg='#212129',fg='#08edff',font=('Helvetica',34))
            form_5_chapter_9_label.grid(row=0,column=1,pady=10)

            percentage_cover_button=tk.Button(biof5c9_frame, text='Percentage Cover', bg='#f08080',font=("Helvetica",24),command=lambda:percentage_cover())
            percentage_cover_button.grid(row=3,column=1,pady=10,sticky='ew')

            backbutton_f5c9=tk.Button(biof5c9_frame, text='Back',bg='#1c6cc0', fg='#FFFFFF',font=("Helvetica",16), command=lambda:backbutton(biof5c9_frame, biof5_frame))
            backbutton_f5c9.grid(row=9,column=1,pady=10)

            population_button=tk.Button(biof5c9_frame, text='Population', bg='#f08080',font=("Helvetica",24),command=lambda:population())
            population_button.grid(row=1,column=1,pady=10,sticky='ew')

            transpiration_rate_button=tk.Button(biof5c9_frame, text='Transpiration Rate', bg='#f08080',font=("Helvetica",24),command=lambda:transpiration_rate())
            transpiration_rate_button.grid(row=2,column=1,pady=10,sticky='ew')
            
            def percentage_cover():
                backbutton(biof5c9_frame, percentage_cover_frame)
                def percentage_cover_calc():
                    number_of_squares_containing_a_species=int(number_of_squares_containing_a_species_entry.get())
                    total_number_of_squares = int(total_number_of_squares_entry.get())
                    if number_of_squares_containing_a_species<0 or total_number_of_squares<0:
                        messagebox.showerror(title='Error',message='input cannot be negative')
                    else:
                        percentage_cover=number_of_squares_containing_a_species/total_number_of_squares*100    
                    result_label.config(text=f"{percentage_cover} %")

                percentage_cover_label=tk.Label(percentage_cover_frame, text='Percentage Cover',  bg="#212129",fg="#08edff",font=("Helvetica",34))
                number_of_squares_containing_a_species_label=tk.Label(percentage_cover_frame, text='Number of Squares Containing a Species', bg="#212129",fg="#f08080",font=("Helvetica",16))    
                total_number_of_squares_label =tk.Label(percentage_cover_frame, text='Total Number of Squares Containing a Species',  bg="#212129",fg="#f08080",font=("Helvetica",16))
                result_label=tk.Label(percentage_cover_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))
                number_of_squares_containing_a_species_entry=tk.Entry(percentage_cover_frame,font=("Helvetica", 16))
                total_number_of_squares_entry=tk.Entry(percentage_cover_frame, font=("Helvetica", 16))
                percentage_cover_back=tk.Button(percentage_cover_frame, text='Back',bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(percentage_cover_frame,biof5c9_frame,result_label))
                percentage_cover_back.grid(row=9, column=1,pady=10)
                calculate_button=tk.Button(percentage_cover_frame,text='Calculate',bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:percentage_cover_calc())
                calculate_button.grid(row=8,column=1,pady=10)
                percentage_cover_label.grid(row=0,column=1,pady=10)
                number_of_squares_containing_a_species_label.grid(row=1,column=0,pady=10)
                total_number_of_squares_label.grid(row=2,column=0,pady=10)
                number_of_squares_containing_a_species_entry.grid(row=1,column=2)
                total_number_of_squares_entry.grid(row=2,column=2,padx=50)
                result_label.grid(row=3, column=1,pady=10)

            def population():
                backbutton(biof5c9_frame, population_frame)
                def population_calc():
                    first_catch_number=int(first_catch_number_entry.get())
                    second_catch_number=int(second_catch_number_entry.get())
                    marked_second_catch_number = int(marked_second_catch_number_entry.get())
                    if first_catch_number<0 or second_catch_number<0 or marked_second_catch_number<0: 
                       messagebox.showerror(title='Error',message='input cannot be negative')
                    else:
                        population=(first_catch_number*second_catch_number)/marked_second_catch_number
                    result_label.config(text=f"{population}")

                population_label=tk.Label(population_frame, text='Population',  bg="#212129",fg="#08edff",font=("Helvetica",34))
                first_catch_number_label=tk.Label(population_frame, text='First Catch Number',bg="#212129",fg="#f08080",font=("Helvetica",24))
                second_catch_number_label=tk.Label(population_frame, text='Second Catch Number',bg="#212129",fg="#f08080",font=("Helvetica",24))
                marked_second_catch_number_label=tk.Label(population_frame, text='Marked Second Catch Number',bg="#212129",fg="#f08080",font=("Helvetica",24))
                result_label=tk.Label(population_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                first_catch_number_entry=tk.Entry(population_frame,font=("Helvetica", 16))
                second_catch_number_entry=tk.Entry(population_frame,font=("Helvetica", 16))
                marked_second_catch_number_entry=tk.Entry(population_frame,font=("Helvetica", 16))

                population_back=tk.Button(population_frame, text='Back',bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(population_frame,biof5c9_frame,result_label))
                population_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(population_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:population_calc())
                calculate_button.grid(row=8,column=1,pady=10)

                population_label.grid(row=0,column=1,pady=10)
                first_catch_number_label.grid(row=1,column=0,pady=10)
                second_catch_number_label.grid(row=2,column=0,pady=10)
                marked_second_catch_number_label.grid(row=3,column=0,pady=10)
                first_catch_number_entry.grid(row=1,column=2,padx=70)
                second_catch_number_entry.grid(row=2,column=2)
                marked_second_catch_number_entry.grid(row=3,column=2)
                result_label.grid(row=4,column=1,pady=10)

            def transpiration_rate():
                backbutton(biof5c9_frame,transpiration_rate_frame)
                def transpiration_rate_calc():
                    distance_moved_by_air_bubble_from_x_to_y = int(distance_moved_by_air_bubble_from_x_to_y_entry.get())
                    time=int(time_entry.get())
                    if time<0 or distance_moved_by_air_bubble_from_x_to_y <0:
                        messagebox.showerror(title="Error", message="input cannot be negative")
                    else:
                        transpiration_rate = distance_moved_by_air_bubble_from_x_to_y/time 
                    result_label.config(text=f"{transpiration_rate} cm/min")

                transpiration_rate_label = tk.Label(transpiration_rate_frame,text="Transpiration Rate",bg="#212129",fg="#08edff",font=("Helvetica",34))
                distance_moved_by_air_bubble_from_x_to_y_label=tk.Label(transpiration_rate_frame,text="Distance Moved by Air Bubble From x to y",bg="#212129",fg="#f08080",font=("Helvetica",16))
                time_label=tk.Label(transpiration_rate_frame,text="Time",bg="#212129",fg="#f08080",font=("Helvetica",16))     
                result_label=tk.Label(transpiration_rate_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                distance_moved_by_air_bubble_from_x_to_y_entry=tk.Entry(transpiration_rate_frame,font=("Helvetica",16))
                time_entry=tk.Entry(transpiration_rate_frame,font=("Helvetica",16))

                transpiration_rate_back=tk.Button(transpiration_rate_frame,text='Back',bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(transpiration_rate_frame,biof5c9_frame,result_label))
                transpiration_rate_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(transpiration_rate_frame,text='Calculate',bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:transpiration_rate_calc())      
                calculate_button.grid(row=8,column=1,pady=10)

                transpiration_rate_label.grid(row=0,column=1,pady=10)
                distance_moved_by_air_bubble_from_x_to_y_label.grid(row=1,column=0,pady=10)
                time_label.grid(row=2,column=0,pady=10)
                distance_moved_by_air_bubble_from_x_to_y_entry.grid(row=1,column=2)
                time_entry.grid(row=2,column=2,padx=50)
                result_label.grid(row=3,column=1,pady=10)

            

        f5Chapter_label=tk.Label(biof5_frame, text="Biology Form 5", bg="#212129",fg="#08edff",font=("Helvetica",34))
        chap9_button=tk.Button(biof5_frame,text="Chapter 9",bg="#f08080", font=("Helvetica",24),command=lambda:bio_f5_chap9()) 

        f5Chapter_label.grid(row=0,column=2,padx=10,pady=10)  
        chap9_button.grid(row=1,column=2,padx=10,pady=50)    
        bio_f5_back=tk.Button(biof5_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(biof5_frame,pack_surface))
        bio_f5_back.grid(row=6,column=2,pady=10) 


    form4_button=tk.Button(bio_frame,text="Form 4", bg="#f08080", font=("Helvetica",24),command=lambda:bio_f4())
    form5_button=tk.Button(bio_frame,text="Form 5", bg="#f08080", font=("Helvetica",24),command=lambda:bio_f5())
    chooseForm_label=tk.Label(bio_frame,text="Choose which form:",bg="#212129",fg="#08edff", font=("Helvetica",34))   
  
    form4_button.grid(row=1,column=0,padx=20,pady=200)
    form5_button.grid(row=1,column=2,padx=20)
    chooseForm_label.grid(row=0,column=1,sticky="ew",padx=10,pady=10)

    bio_back = tk.Button(bio_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(pack_surface,forget_surface))
    bio_back.grid(row=6,column=1)  

#form 4 only
def f4_PhysicsPage(forget_surface):
    def phy_f4():
        backbutton(forget_surface,f4_phyf4_frame)
        def phy_f4_chap2():
            backbutton(f4_phyf4_frame,f4_phyf4c2_frame)
            def speed():
                backbutton(f4_phyf4c2_frame,f4_speed_frame)
                def speed_calc():
                    distance=float(distance_entry.get())
                    time = float(time_entry.get())
                    if distance<0 or time<0:
                        messagebox.showerror(title="Error", message="Distance or time cannot be negative")
                    else:
                        speed=abs(distance/time)
                    result_label.config(text=f"{speed} m/s")


                speed_label=tk.Label(f4_speed_frame, text="Speed", bg="#212129",fg="#08edff",font=("Helvetica",34))
                distance_label=tk.Label(f4_speed_frame,text="Distance",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                time_label=tk.Label(f4_speed_frame,text="Time taken",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(f4_speed_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))
                

                distance_entry=tk.Entry(f4_speed_frame, font=("Helvetica", 16))
                time_entry=tk.Entry(f4_speed_frame, font=("Helvetica", 16))

                speed_back=tk.Button(f4_speed_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(f4_speed_frame,f4_phyf4c2_frame,result_label))
                speed_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(f4_speed_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:speed_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                speed_label.grid(row=0,column=1,pady=10,padx=20)
                distance_label.grid(row=1,column=0,pady=10,padx=20)
                time_label.grid(row=2,column=0,pady=10,padx=50)

                distance_entry.grid(row=1,column=2,padx=20)
                time_entry.grid(row=2,column=2,padx=20)
                result_label.grid(row=3,column=1,pady=10)

            def velocity():
                backbutton(f4_phyf4c2_frame,f4_velocity_frame)
                def velocity_calc():
                    displacement=float(displacement_entry.get())
                    time = float(time_entry.get())
                    if time<0:
                        messagebox.showerror(title="Error", message="Time cannot be negative")
                    if time>0:
                        velocity=displacement/time
                    result_label.config(text=f"{velocity} m/s")


                velocity_label=tk.Label(f4_velocity_frame, text="Velocity", bg="#212129",fg="#08edff",font=("Helvetica",34))
                displacement_label=tk.Label(f4_velocity_frame,text="Displacement",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                time_label=tk.Label(f4_velocity_frame,text="Time taken",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(f4_velocity_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                displacement_entry=tk.Entry(f4_velocity_frame, font=("Helvetica", 16))
                time_entry=tk.Entry(f4_velocity_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(f4_velocity_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(f4_velocity_frame,f4_phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(f4_velocity_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:velocity_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                velocity_label.grid(row=0,column=1,pady=20,padx=20)
                displacement_label.grid(row=1,column=0,pady=20,padx=40)
                time_label.grid(row=2,column=0,pady=20,padx=20)

                displacement_entry.grid(row=1,column=2,padx=20)
                time_entry.grid(row=2,column=2,padx=20)
                result_label.grid(row=3,column=1,pady=10)
            
            def acceleration():
                backbutton(f4_phyf4c2_frame,f4_acceleration_frame)
                def acceleration_calc():
                    v=float(fin_vel_entry.get())
                    u=float(ini_vel_entry.get())
                    t = float(time_entry.get())
                    if t<0:
                        messagebox.showerror(title="Error", message="Time cannot be negative")
                    if t>0:
                        acceleration=(v-u)/t
                    result_label.config(text=f"{acceleration} m/s^2")


                acceleration_label=tk.Label(f4_acceleration_frame, text="Acceleration", bg="#212129",fg="#08edff",font=("Helvetica",34))
                ini_vel_label=tk.Label(f4_acceleration_frame,text="Initial Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                fin_vel_label=tk.Label(f4_acceleration_frame,text="Final Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                time_label=tk.Label(f4_acceleration_frame,text="Time taken",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(f4_acceleration_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                ini_vel_entry=tk.Entry(f4_acceleration_frame, font=("Helvetica", 16))
                fin_vel_entry=tk.Entry(f4_acceleration_frame, font=("Helvetica", 16))
                time_entry=tk.Entry(f4_acceleration_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(f4_acceleration_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(f4_acceleration_frame,f4_phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(f4_acceleration_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:acceleration_calc())
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
                backbutton(f4_phyf4c2_frame,f4_momentum_frame)
                def momentum_calc():
                    v=float(vel_entry.get())
                    m=float(mass_entry.get())
                    if m<0:
                        messagebox.showerror(title="Error", message="Mass cannot be negative")
                    else:
                        momentum=m*v
                    result_label.config(text=f"{momentum} kg m/s")


                momentum_label=tk.Label(f4_momentum_frame, text="Momentum", bg="#212129",fg="#08edff",font=("Helvetica",34))
                vel_label=tk.Label(f4_momentum_frame,text="Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                mass_label=tk.Label(f4_momentum_frame,text="Mass",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(f4_momentum_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                vel_entry=tk.Entry(f4_momentum_frame, font=("Helvetica", 16))
                mass_entry=tk.Entry(f4_momentum_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(f4_momentum_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(f4_momentum_frame,f4_phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(f4_momentum_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:momentum_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                momentum_label.grid(row=0,column=1,pady=10,padx=20)
                vel_label.grid(row=1,column=0,pady=10,padx=70)
                mass_label.grid(row=2,column=0,pady=10,padx=20)

                vel_entry.grid(row=1,column=2,padx=20)
                mass_entry.grid(row=2,column=2,padx=20)
                result_label.grid(row=3,column=1,pady=10)

            def force():
                backbutton(f4_phyf4c2_frame,f4_force_frame)
                def force_calc():
                    m=float(mass_entry.get())
                    a=float(acc_entry.get())
                    if m<0:
                        messagebox.showerror(title="Error", message="Mass cannot be negative")
                    else:
                        force=m*a
                    result_label.config(text=f"{force} N")


                force_label=tk.Label(f4_force_frame, text="Force", bg="#212129",fg="#08edff",font=("Helvetica",34))
                mass_label=tk.Label(f4_force_frame,text="Mass",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                acc_label=tk.Label(f4_force_frame,text="Acceleration",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(f4_force_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                mass_entry=tk.Entry(f4_force_frame, font=("Helvetica", 16))
                acc_entry=tk.Entry(f4_force_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(f4_force_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(f4_force_frame,f4_phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(f4_force_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:force_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                force_label.grid(row=0,column=1,pady=10,padx=20)
                mass_label.grid(row=1,column=0,pady=10,padx=20)
                acc_label.grid(row=2,column=0,pady=10,padx=50)

                mass_entry.grid(row=1,column=2,padx=20)
                acc_entry.grid(row=2,column=2,padx=20)
                result_label.grid(row=3,column=1,pady=10)

            def impulse():
                backbutton(f4_phyf4c2_frame,f4_impulse_frame)
                def impulse_calc():
                    m=float(mass_entry.get())
                    v=float(fin_vel_entry.get())
                    u=float(ini_vel_entry.get())
                    if m<0:
                        messagebox.showerror(title="Error", message="Mass cannot be negative")
                    else:
                        impulse=m*v-m*u
                    result_label.config(text=f"{impulse} N/s")


                impulse_label=tk.Label(f4_impulse_frame, text="Impulse", bg="#212129",fg="#08edff",font=("Helvetica",34))
                fin_vel_label=tk.Label(f4_impulse_frame,text="Final Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                ini_vel_label=tk.Label(f4_impulse_frame,text="Initial Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                mass_label=tk.Label(f4_impulse_frame,text="Mass",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(f4_impulse_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                fin_vel_entry=tk.Entry(f4_impulse_frame, font=("Helvetica", 16))
                ini_vel_entry=tk.Entry(f4_impulse_frame, font=("Helvetica", 16))
                mass_entry=tk.Entry(f4_impulse_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(f4_impulse_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(f4_impulse_frame,f4_phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(f4_impulse_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:impulse_calc())
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
                backbutton(f4_phyf4c2_frame,f4_impulsiveForce_frame)
                def impulsiveForce_calc():
                    m=float(mass_entry.get())
                    v=float(fin_vel_entry.get())
                    u=float(ini_vel_entry.get())
                    t=float(time_entry.get())
                    if m<0 or t<0:
                        messagebox.showerror(title="Error", message="Mass or time cannot be negative")
                    else:
                        impulsiveForce=(m*v-m*u)/t
                    result_label.config(text=f"{impulsiveForce} N")


                impulsiveForce_label=tk.Label(f4_impulsiveForce_frame, text="Impulsive Force", bg="#212129",fg="#08edff",font=("Helvetica",34))
                fin_vel_label=tk.Label(f4_impulsiveForce_frame,text="Final Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                ini_vel_label=tk.Label(f4_impulsiveForce_frame,text="Initial Velocity",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                mass_label=tk.Label(f4_impulsiveForce_frame,text="Mass",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                time_label=tk.Label(f4_impulsiveForce_frame,text="Time",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(f4_impulsiveForce_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                fin_vel_entry=tk.Entry(f4_impulsiveForce_frame, font=("Helvetica", 16))
                ini_vel_entry=tk.Entry(f4_impulsiveForce_frame, font=("Helvetica", 16))
                mass_entry=tk.Entry(f4_impulsiveForce_frame, font=("Helvetica", 16))
                time_entry=tk.Entry(f4_impulsiveForce_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(f4_impulsiveForce_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(f4_impulsiveForce_frame,f4_phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(f4_impulsiveForce_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:impulsiveForce_calc())
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
                backbutton(f4_phyf4c2_frame,f4_weight_frame)
                def weight_calc():
                    m=float(mass_entry.get())
                    if m<0:
                        messagebox.showerror(title="Error", message="Mass cannot be negative")
                    else:
                        weight=m*9.81
                    result_label.config(text=f"{weight} N")


                weight_label=tk.Label(f4_weight_frame, text="Weight", bg="#212129",fg="#08edff",font=("Helvetica",34))
                mass_label=tk.Label(f4_weight_frame,text="Mass",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                result_label=tk.Label(f4_weight_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                mass_entry=tk.Entry(f4_weight_frame, font=("Helvetica", 16))

                velocity_back=tk.Button(f4_weight_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(f4_weight_frame,f4_phyf4c2_frame,result_label))
                velocity_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(f4_weight_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:weight_calc())
                calculate_button.grid(row=8,column=1,pady=10)


                weight_label.grid(row=0,column=1,pady=10,padx=20)
                mass_label.grid(row=1,column=0,pady=10,padx=100)

                mass_entry.grid(row=1,column=2,padx=20)
                result_label.grid(row=2,column=1,pady=10)
            
            f4Chapter2_label=tk.Label(f4_phyf4c2_frame, text="Physics Form 4 Chapter 2", bg="#212129",fg="#08edff",font=("Helvetica",34))
            speed_button=tk.Button(f4_phyf4c2_frame,text="Speed",bg="#90ee90", font=("Helvetica",24),command=lambda:speed())
            velocity_button=tk.Button(f4_phyf4c2_frame,text="Velocity",bg="#90ee90", font=("Helvetica",24),command=lambda:velocity())
            acceleration_button=tk.Button(f4_phyf4c2_frame,text="Acceleration",bg="#90ee90", font=("Helvetica",24),command=lambda:acceleration())
            momentum_button=tk.Button(f4_phyf4c2_frame,text="Momentum",bg="#90ee90", font=("Helvetica",24),command=lambda:momentum())
            force_button=tk.Button(f4_phyf4c2_frame,text="Force",bg="#90ee90", font=("Helvetica",24),command=lambda:force())
            impulse_button=tk.Button(f4_phyf4c2_frame,text="Impulse",bg="#90ee90", font=("Helvetica",24),command=lambda:impulse())
            impulsive_force_button=tk.Button(f4_phyf4c2_frame,text="Impulsive Force",bg="#90ee90", font=("Helvetica",24),command=lambda:impulsiveForce())
            weight_button=tk.Button(f4_phyf4c2_frame,text="Weight",bg="#90ee90", font=("Helvetica",24),command=lambda:weight())

            phy_f4c2_back=tk.Button(f4_phyf4c2_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(f4_phyf4c2_frame,f4_phyf4_frame))
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
            
        f4Chapter_label=tk.Label(f4_phyf4_frame, text="Physics Form 4", bg="#212129",fg="#08edff",font=("Helvetica",34))
        chap2_button=tk.Button(f4_phyf4_frame,text="Chapter 2",bg="#90ee90", font=("Helvetica",24),command=lambda:phy_f4_chap2())
        chap3_button=tk.Button(f4_phyf4_frame,text="Chapter 3",bg="#adb0b4", font=("Helvetica",24))
        chap4_button=tk.Button(f4_phyf4_frame,text="Chapter 4",bg="#adb0b4", font=("Helvetica",24))
        chap5_button=tk.Button(f4_phyf4_frame,text="Chapter 5",bg="#adb0b4", font=("Helvetica",24))
        chap6_button=tk.Button(f4_phyf4_frame,text="Chapter 6",bg="#adb0b4", font=("Helvetica",24))

        phy_f4_back=tk.Button(f4_phyf4_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(f4_phyf4_frame,f4_subject_frame))
        phy_f4_back.grid(row=6,column=2,pady=40)

        f4Chapter_label.grid(row=0,column=2,padx=10,pady=10)
        chap2_button.grid(row=1,column=0,padx=20,pady=50)
        chap3_button.grid(row=1,column=2,padx=20)
        chap4_button.grid(row=1,column=4,padx=20)
        chap5_button.grid(row=2,column=1,padx=20,pady=50)
        chap6_button.grid(row=2,column=3,padx=20)
    phy_f4()

def f4_ChemistryPage(forget_surface):

    def chem_f4():
        backbutton(forget_surface,f4_chemf4_frame)
        def chem_f4_chap2():
            backbutton(f4_chemf4_frame,f4_chemf4c2_frame)
            def nucleon_number():
                backbutton(f4_chemf4c2_frame, f4_nucleon_frame)
                def nucleon_calc():
                    number_of_protons=int(number_of_protons_entry.get())
                    number_of_neutrons=int(number_of_neutrons_entry.get())
                    if number_of_protons <0 or number_of_neutrons <0:
                        messagebox.showerror(title="Error", message="Number of protons and number of neutrons cannot be negative")
                    else:
                        nucleon=number_of_protons + number_of_neutrons
                    result_label.config(text=f"{nucleon}")


                nucleon_label=tk.Label(f4_nucleon_frame, text="Nucleon Number", bg="#212129",fg="#08edff",font=("Helvetica",34))
                number_of_protons_label=tk.Label(f4_nucleon_frame,text="Number of Protons",bg="#212129",fg="#add8e6", font=("Helvetica", 24))
                number_of_neutrons_label=tk.Label(f4_nucleon_frame,text="Number of Neutrons",bg="#212129",fg="#add8e6", font=("Helvetica", 24))
                result_label=tk.Label(f4_nucleon_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                number_of_protons_entry=tk.Entry(f4_nucleon_frame, font=("Helvetica", 16))
                number_of_neutrons_entry=tk.Entry(f4_nucleon_frame, font=("Helvetica", 16))

                nucleon_back=tk.Button(f4_nucleon_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(f4_nucleon_frame,f4_chemf4c2_frame,result_label))
                nucleon_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(f4_nucleon_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:nucleon_calc())
                calculate_button.grid(row=8,column=1,pady=10)

                nucleon_label.grid(row=0,column=1,pady=10,padx=20)
                number_of_protons_label.grid(row=1,column=0,pady=10,padx=10)
                number_of_neutrons_label.grid(row=2,column=0,pady=10,padx=10)

                number_of_protons_entry.grid(row=1,column=2,padx=20)
                number_of_neutrons_entry.grid(row=2,column=2,padx=20)
                result_label.grid(row=3,column=1,padx=20)

            f4Chapter2_label=tk.Label(f4_chemf4c2_frame, text="Chemistry Form 4 Chapter 2", bg="#212129",fg="#08edff",font=("Helvetica",34))
            nucleon_number_button=tk.Button(f4_chemf4c2_frame,text="Nucleon Number",bg="#add8e6", font=("Helvetica",24),command=lambda:nucleon_number())
            

            chem_f4c2_back=tk.Button(f4_chemf4c2_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(f4_chemf4c2_frame,f4_chemf4_frame))
            chem_f4c2_back.grid(row=9,column=1,pady=10)


            f4Chapter2_label.grid(row=0,column=1,padx=20,pady=10)
            nucleon_number_button.grid(row=1,column=1,pady=10,sticky="ew",padx=20)          
                    

        f4Chapter_label=tk.Label(f4_chemf4_frame, text="Chemistry Form 4", bg="#212129",fg="#08edff",font=("Helvetica",34))
        chap2_button=tk.Button(f4_chemf4_frame,text="Chapter 2",bg="#add8e6", font=("Helvetica",24),command=lambda:chem_f4_chap2())
        chap3_button=tk.Button(f4_chemf4_frame,text="Chapter 3",bg="#adb0b4", font=("Helvetica",24))
        chap4_button=tk.Button(f4_chemf4_frame,text="Chapter 4",bg="#adb0b4", font=("Helvetica",24))
        chap5_button=tk.Button(f4_chemf4_frame,text="Chapter 5",bg="#adb0b4", font=("Helvetica",24))
        chap6_button=tk.Button(f4_chemf4_frame,text="Chapter 6",bg="#adb0b4", font=("Helvetica",24))
        chap7_button=tk.Button(f4_chemf4_frame,text="Chapter 7",bg="#adb0b4", font=("Helvetica",24))
        chap8_button=tk.Button(f4_chemf4_frame,text="Chapter 8",bg="#adb0b4", font=("Helvetica",24))
        

        chem_f4_back=tk.Button(f4_chemf4_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(f4_chemf4_frame,f4_subject_frame))
        chem_f4_back.grid(row=6,column=2,pady=40)

        f4Chapter_label.grid(row=0,column=2,padx=10,pady=10)
        chap2_button.grid(row=1,column=0,padx=20,pady=50)
        chap3_button.grid(row=1,column=2,padx=20)
        chap4_button.grid(row=1,column=4,padx=20)
        chap5_button.grid(row=2,column=0,padx=20,pady=50)
        chap6_button.grid(row=2,column=2,padx=20)
        chap7_button.grid(row=2,column=4,padx=20)
        chap8_button.grid(row=3,column=2,padx=20,pady=50)
    chem_f4()

def f4_BiologyPage(forget_surface):
    #backbutton(forget_surface,pack_surface)
    def bio_f4():
        backbutton(forget_surface,f4_biof4_frame)
        def bio_f4_chap4():
            backbutton(f4_biof4_frame,f4_biof4c4_frame)

            form_4_chapter_4_label=tk.Label(f4_biof4c4_frame, text='Biology form 4 chapter 2 ', bg="#212129",fg="#08edff",font=("Helvetica",34))
            form_4_chapter_4_label.grid(row=0,column=1,pady=10,padx=20)
            percentage_diff_in_mass_button=tk.Button(f4_biof4c4_frame, text='Percentage difference in mass', bg="#f08080", font=("Helvetica",24), command=lambda:percentage_diff_in_mass())
            percentage_diff_in_mass_button.grid(row=1,column=1,pady=10,padx=20,sticky="ew")
            backbutton_f4c4=tk.Button(f4_biof4c4_frame, text='Back', bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16) ,command=lambda:backbutton(f4_biof4c4_frame,f4_biof4_frame) )
            backbutton_f4c4.grid(row=9,column=1,pady=10)

            def percentage_diff_in_mass():
                backbutton(f4_biof4c4_frame, f4_percentage_diff_in_mass_frame)
                def percentage_difference_in_mass_calc():
                    final_mass = int(final_mass_entry.get())
                    initial_mass = int(initial_mass_entry.get())
                    if final_mass<0 or initial_mass<0:
                        messagebox.showerror(title="Error", message="final or initial mass cannot be negative")
                    else:
                            percentage_difference_in_mass = ((final_mass-initial_mass)/initial_mass)*0.01
                    result_label.config(text=f"{percentage_difference_in_mass} %")
                
                percentage_diff_in_mass_label = tk.Label(f4_percentage_diff_in_mass_frame, text="Percentage Difference in Mass",bg="#212129",fg="#08edff",font=("Helvetica",34))
                final_mass_label= tk.Label(f4_percentage_diff_in_mass_frame,text="Final mass",bg="#212129",fg="#f08080", font=("Helvetica", 24))
                initial_mass_label = tk.Label(f4_percentage_diff_in_mass_frame,text="Initial mass",bg="#212129",fg="#f08080", font=("Helvetica", 24)) 
                result_label = tk.Label(f4_percentage_diff_in_mass_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))
                final_mass_entry = tk.Entry(f4_percentage_diff_in_mass_frame, font=("Helvetica", 16))
                initial_mass_entry = tk.Entry(f4_percentage_diff_in_mass_frame, font=("Helvetica", 16))
                percentage_diff_in_mass_back = tk.Button(f4_percentage_diff_in_mass_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(f4_percentage_diff_in_mass_frame,f4_biof4c4_frame,result_label))
                percentage_diff_in_mass_back.grid(row=9,column=1,pady=10)
                calculate_button = tk.Button(f4_percentage_diff_in_mass_frame, text='Calculate',bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:percentage_difference_in_mass_calc())
                calculate_button.grid(row=8,column=1,pady=10)
                percentage_diff_in_mass_label.grid(row=0, column=1,pady=10)
                final_mass_label.grid(row=1,column=0, pady=10,padx=20)
                initial_mass_label.grid(row=2, column=0,pady=10,padx=20)
                final_mass_entry.grid(row=1,column=2,padx=20)
                initial_mass_entry.grid(row=2, column=2,padx=20)
                result_label.grid(row=3,column=1,pady=10,padx=20)

        def bio_f4_chap5():
            backbutton(f4_biof4_frame,f4_biof4c5_frame)

            form_4_chapter_5_label=tk.Label(f4_biof4c5_frame,text='Biology Form 4 Chapter 5' ,bg="#212129",fg="#08edff",font=("Helvetica",34))
            form_4_chapter_5_label.grid(row=0,column=1,pady=10,padx=20)
            enzyme_reaction_rate_button=tk.Button(f4_biof4c5_frame,text='Enzyme Reaction Rate', bg="#f08080", font=("Helvetica",24),command=lambda:enzyme_reaction_rate())
            enzyme_reaction_rate_button.grid(row=1,column=1,pady=10,padx=20,sticky="ew")
            backbutton_f4c5=tk.Button(f4_biof4c5_frame, text='Back' , bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:backbutton(f4_biof4c5_frame,f4_biof4_frame))
            backbutton_f4c5.grid(row=9,column=1,pady=10)

            def enzyme_reaction_rate():
                backbutton(f4_biof4c5_frame, f4_enzyme_reaction_rate_frame)
                def enzyme_reaction_rate_calc():
                    time_taken=int(time_entry.get())    
                    if time_taken<0:
                        messagebox.showerror(title="Error", message="time cannot be negative")
                    else:
                         enzyme_reaction_rate = 1/time_taken
                    rounded_rate=round(enzyme_reaction_rate,4)
                    result_label.config(text=f"{rounded_rate} s") 
                enzyme_reaction_rate_label=tk.Label(f4_enzyme_reaction_rate_frame, text='Enzyme Reaction Rate',bg="#212129",fg="#08edff",font=("Helvetica",34) )    
                time_label=tk.Label(f4_enzyme_reaction_rate_frame,text='Time',bg="#212129",fg="#f08080",font=("Helvetica",34))
                result_label=tk.Label(f4_enzyme_reaction_rate_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))
                time_entry=tk.Entry(f4_enzyme_reaction_rate_frame, font=("Helvetica", 16))
                enzyme_reaction_rate_back=tk.Button(f4_enzyme_reaction_rate_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(f4_enzyme_reaction_rate_frame,f4_biof4c5_frame,result_label))
                enzyme_reaction_rate_back.grid(row=9, column=1, pady=10)
                calculate_button=tk.Button(f4_enzyme_reaction_rate_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:enzyme_reaction_rate_calc())
                calculate_button.grid(row=8,column=1,pady=10)
                enzyme_reaction_rate_label.grid(row=0,column=1,pady=10)
                time_label.grid(row=1,column=0,pady=10,padx=70)
                time_entry.grid(row=1,column=2,padx=20)
                result_label.grid(row=3,column=1,pady=10,padx=20)
        def bio_f4_chap7():
            backbutton(f4_biof4_frame, f4_biof4c7_frame)

            form_4_chapter_7_label = tk.Label(f4_biof4c7_frame, text='Biology Form 4 Chapter 7', bg="#212129",fg="#08edff",font=("Helvetica",34))
            form_4_chapter_7_label.grid(row=0,column=1,pady=10,padx=20)

            energy_value_food_sample_button = tk.Button(f4_biof4c7_frame, text='Energy Value Food Sample', bg="#f08080", font=("Helvetica",24), command=lambda: energy_value_food_sample())
            energy_value_food_sample_button.grid(row=1,column=1,pady=10,sticky="ew",padx=20)

            backbutton_f4c7 = tk.Button(f4_biof4c7_frame, text='Back',  bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda: backbutton(f4_biof4c7_frame, f4_biof4_frame))
            backbutton_f4c7.grid(row=9,column=1,pady=10,padx=20)

            def energy_value_food_sample():
                backbutton(f4_biof4c7_frame, f4_energy_value_food_sample_frame)
                def energy_value_food_sample_calc():
                    try:
                        mass_water = int(mass_water_entry.get())
                        temperature_rise = int(temperature_rise_entry.get())
                        mass_food = int(mass_food_entry.get())
                        if mass_food < 0 or mass_water < 0 or temperature_rise < 0:
                            messagebox.showerror(title='Error', message="Mass of water, food, and temperature rise cannot be negative")
                        else:
                            energy_value_food_sample = (4.2 * mass_water * temperature_rise) / mass_food * 1000
                            result_label.config(text=f"Energy Value: {energy_value_food_sample:.2f} J/g")
                    except ValueError:
                        messagebox.showerror(title='Error', message="Please enter valid numbers")
                energy_value_food_sample_label = tk.Label(f4_energy_value_food_sample_frame, text='Energy Value Food Sample', bg="#212129", fg="#08edff", font=("Helvetica", 34))
                energy_value_food_sample_label.grid(row=0, column=1, pady=10)
                mass_water_label = tk.Label(f4_energy_value_food_sample_frame, text='Mass Water (g)', bg="#212129", fg="#f08080", font=("Helvetica", 24))
                mass_water_label.grid(row=1, column=0, pady=10)
                mass_water_entry = tk.Entry(f4_energy_value_food_sample_frame, font=("Helvetica", 16))
                mass_water_entry.grid(row=1, column=2, pady=10)
                temperature_rise_label = tk.Label(f4_energy_value_food_sample_frame, text='Temperature Rise (°C)', bg="#212129", fg="#f08080", font=("Helvetica", 24))
                temperature_rise_label.grid(row=2, column=0, pady=10,padx=20)
                temperature_rise_entry = tk.Entry(f4_energy_value_food_sample_frame, font=("Helvetica", 16))
                temperature_rise_entry.grid(row=2, column=2, pady=10)
                mass_food_label = tk.Label(f4_energy_value_food_sample_frame, text='Mass Food (g)', bg="#212129", fg="#f08080", font=("Helvetica", 24))
                mass_food_label.grid(row=3, column=0, pady=10)
                mass_food_entry = tk.Entry(f4_energy_value_food_sample_frame, font=("Helvetica", 16))
                mass_food_entry.grid(row=3, column=2, pady=10,padx=50)
                calculate_button = tk.Button(f4_energy_value_food_sample_frame, text="Calculate", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=energy_value_food_sample_calc)
                calculate_button.grid(row=5, column=1, pady=10)
                result_label = tk.Label(f4_energy_value_food_sample_frame, text='', bg="#212129", fg="#FFFFFF", font=("Helvetica", 24))
                result_label.grid(row=4, column=1, pady=10)
                energy_value_food_sample_back = tk.Button(f4_energy_value_food_sample_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda: backbutton_delresult(f4_energy_value_food_sample_frame, f4_biof4c7_frame,result_label))
                energy_value_food_sample_back.grid(row=6, column=1, pady=10)
                
        f4Chapter_label=tk.Label(f4_biof4_frame, text="Biology Form 4", bg="#212129",fg="#08edff",font=("Helvetica",34))
        chap4_button=tk.Button(f4_biof4_frame,text="Chapter 4",bg="#f08080", font=("Helvetica",24),command=lambda:bio_f4_chap4())
        chap5_button=tk.Button(f4_biof4_frame,text="Chapter 5",bg="#f08080", font=("Helvetica",24),command=lambda:bio_f4_chap5())
        chap7_button=tk.Button(f4_biof4_frame,text="Chapter 7",bg="#f08080", font=("Helvetica",24),command=lambda:bio_f4_chap7())
        bio_f4_back=tk.Button(f4_biof4_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton(f4_biof4_frame,f4_subject_frame))
        bio_f4_back.grid(row=6,column=2,pady=10)
        
        f4Chapter_label.grid(row=0,column=2,padx=10,pady=10)  
        chap4_button.grid(row=1,column=0,padx=10,pady=50)
        chap5_button.grid(row=1,column=2,padx=10)
        chap7_button.grid(row=1,column=4,padx=10)

    bio_f4()


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

