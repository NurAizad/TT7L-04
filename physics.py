import SPM_Calc

global phyf4_frame
global phyf4c2_frame
global backbutton
global acceleration_frame
import tkinter as tk

print("yay")
def acc():
    print ("uwu")
    SPM_Calc.backbutton(SPM_Calc.phyf4c2_frame,SPM_Calc.acceleration_frame)
    def speed_calc():
        distance=float(distance_entry.get())
        time = float(time_entry.get())
        speed=distance/time
        result_label.config(text=f"{speed}")


    speed_label=tk.Label(SPM_Calc.acceleration_frame, text="Physics Form 4 Chapter 2", bg="#212129",fg="#08edff",font=("Helvetica",34))
    distance_label=tk.Label(SPM_Calc.acceleration_frame,text="Distance",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
    time_label=tk.Label(SPM_Calc.acceleration_frame,text="Time taken",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
    result_label=tk.Label(SPM_Calc.acceleration_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))
    

    distance_entry=tk.Entry(SPM_Calc.acceleration_frame, font=("Helvetica", 16))
    time_entry=tk.Entry(SPM_Calc.acceleration_frame, font=("Helvetica", 16))

    speed_back=tk.Button(SPM_Calc.acceleration_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:SPM_Calc.backbutton_delresult(SPM_Calc.acceleration_frame,SPM_Calc.phyf4c2_frame,result_label))
    speed_back.grid(row=9,column=1,pady=10)
    calculate_button=tk.Button(SPM_Calc.acceleration_frame,text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:speed_calc())
    calculate_button.grid(row=8,column=1,pady=10)


    speed_label.grid(row=0,column=1,pady=10)
    distance_label.grid(row=1,column=0,pady=10)
    time_label.grid(row=2,column=0,pady=10)
    distance_entry.grid(row=1,column=2)
    time_entry.grid(row=2,column=2)
    result_label.grid(row=3,column=1,pady=10)
'''
def backbutton(forgetSurface,packSurface):
    forgetSurface.pack_forget()
    packSurface.pack()

def backbutton_delresult(forgetSurface,packSurface,result_label):
    result_label.config(text="")
    forgetSurface.pack_forget()
    packSurface.pack()
'''
