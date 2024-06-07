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
def BiologyPage(forget_surface, pack_surface):
    backbutton(subject_frame,bio_frame)
    def bio_f4():
        backbutton(bio_frame,biof4_frame)
        def bio_f4_chap4():
            backbutton(biof4_frame,biof4c4_frame)
            def percentage_diff_in_mass():
                backbutton(biof4c4_frame, percentage_diff_in_mass_frame)
                def percentage_difference_in_mass_calc():
                    final_mass = int(entry_enter_final_mass.get())
                    initial_mass = int(entry_enter_initial_mass.get())
                    if final_mass<0 or initial_mass<0:
                      messagebox.showerror(title="Error", message="final or initial mass cannot be negative")
                    else:
                         percentage_difference_in_mass = ((final_mass-initial_mass)/initial_mass)*0.01
                    result_label.config(text=f"{percentage_difference_in_mass}")
                
                percentage_diff_in_mass_label = tk.Label(percentage_diff_in_mass_frame, text="percentage difference in mass",bg="#212129",fg="#08edff",font=("Helvetica",34))
                final_mass_label= tk.Label(percentage_diff_in_mass_frame,text="final mass",bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                initial_mass_label = tk.Label(percentage_diff_in_mass_frame,text="initial mass",bg="#212129",fg="#90ee90", font=("Helvetica", 24)) 
                result_label = tk.Label(percentage_diff_in_mass_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                final_mass_entry = tk.Entry(speed_frame, font=("Helvetica", 16))
                initial_mass_entry = tk.Entry(speed_frame, font=("Helvetica", 16))

                percentage_diff_in_mass_back = tk.Button(percentage_diff_in_mass_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(percentage_diff_in_mass_frame,biof4c4_frame,result_label))
                percentage_diff_in_mass_back.grid(row=9,column=1,pady=10)
                calculate_button = tk.Button(percentage_diff_in_mass_frame, text='calculate',bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:percentage_diff_in_mass_calc())
                calculate_button.grid(row=8,column=1,pady=10)

                percentage_diff_in_mass_label.grid(row=0, column=1,pady=10)
                final_mass_label.grid(row=1,column=0, pady=10)
                initial_mass_label.grid(row=2, column=0,pady=10)
                final_mass_entry.grid(row=1,column=2)
                initial_mass_entry.grid(row=2, column=2)
                result_label.grid(row=3,column=1,pady=10)
        def bio_f4_chap5():
            backbutton(biof4_frame,biof4c5_frame)
            def enzyme_reaction_rate():
                backbutton(biof4c5_frame, enzyme_reaction_rate_frame)
                def enzyme_reaction_rate_calc():
                    time_taken=int(entry_time_taken.get())    
                    if time_taken<0:
                        messagebox.showerror(title="Error", message="time cannot be negative")
                    else:
                     enzyme_reaction_rate = 1/time_taken
                rounded_rate=round(enzyme_reaction_rate,4)
                result_label.config(text=f"{rounded_rate}") 

                enzyme_reaction_rate_label=tk.Label(enzyme_reaction_rate_frame, text='enzyme reaction rate',bg="#212129",fg="#08edff",font=("Helvetica",34) )    
                time_label=tk.Label(enzyme_reaction_rate_frame,text='time'bg="#212129",fg="#08edff",font=("Helvetica",34))
                result_label=tk.Label(enzyme_reaction_rate_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                time_entry=tk.Entry(enzyme_reaction_rate_frame, font=("Helvetica", 16))

                enzyme_reaction_rate_back=tk.Button(percentage_diff_in_mass_frame, text="Back", bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(enzyme_reaction_rate_frame,biof4c5_frame,result_label))
                enzyme_reaction_rate_back.grid(row=9, column=1, pady=10)
                calculate_button=tk.Button(enzyme_reaction_rate_frame,text="calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:enzyme_reaction_rate_calc())
                calculate_button.grid(row=8,column=1,pady=10)

                enzyme_reaction_rate_label.grid(row=0,column=1,pady=10)
                time_label.grid(row=1,column=0,pady=10)
                time_entry.grid(row=1,column=2)
                result_label.grid(row=3,column=1,pady=10)

        def bio_f4_chap7():
            backbutton(biof4_frame,biof4c7_frame)  
            def energy_value_food_sample():
                backbutton(biof4c7_frame, energy_food_value_frame)
                def energy_value_food_sample_calc():
                    mass_water=int(entry_mass_water.get())
                    temperature_rise=(entry_temperature_rise.get())
                    mass_food=(entry_mass_food.get())
                    if mass_food<0, mass_water<0 or temperature_rise<0:
                       messagebox.showerroe(title='Error',message="mass water,food and temperature rise cannot be negative")
                    else:
                        energy_value_food_sample = ((4.2*mass_water*temperature_rise)/mass_food*1000)   
                    result_label.config(text=f{energy_value_food_sample})

                energy_value_food_sample_label=tk.Label(energy_value_food_sample_frame, text='energy value food sample',bg="#212129",fg="#08edff",font=("Helvetica",34))
                mass_water_label = tk.Label(energy_value_food_sample_frame, text='mass water',bg="#212129",fg="#90ee90", font=("Helvetica", 24))
                temperature_rise_label =tk.Label(energy_value_food_sample_frame,text='temperature rise',bg="#212129",fg="#90ee90", font=("Helvetica", 24))    
                mass_food_label= tk.Label(energy_value_food_sample_frame,text='mass food',bg="#212129",fg="#90ee90", font=("Helvetica", 24))

                mass_water_entry=tk.Entry(energy_value_food_sample_frame,font=("Helvetica", 16))
                temperature_rise_entry = tk.Entry(energy_value_food_sample_frame, font=("Helvetica",16))
                mass_food_entry = tk.Entry(energy_value_food_sample_frame,font=("Helvetica", 16))

                energy_value_food_sample_back = tk.Button(energy_value_food_sample_frame, text="Back",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(energy_value_food_sample_frame,biof4c7_frame,result_label))
                energy_value_food_sample_back.grid(row=9, column=1,pady=10)
                calculate_button=tk.Button(energy_value_food_sample_frame, text="Calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:energy_value_food_sample_calc())
                calculate_button.grid(row=8, column=1, pady=10)

                energy_value_food_sample_label.grid(row=0,column=1,pady=10)
                mass_water_label.grid(row=1,column=0, pady=10)
                temperature_rise_label.grid(row=2,column=0, pady=10)
                mass_food_label.grid(row=3, column=0,pady=10)
                mass_water_entry.grid(row=1,column=2)
                temperature_rise_entry.grid(row=2,column=2)
                mass_food_entry.grid(row=3,column=3)
                result_label.grid(row=3,column=1,pady=10)
