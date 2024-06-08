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
                    final_mass = int(final_mass_entry.get())
                    initial_mass = int(initial_mass_entry.get())
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
                    time_taken=int(time_entry.get())    
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
                    mass_water=int(mass_water_entry.get())
                    temperature_rise=(temperature_rise_entry.get())
                    mass_food=(mass_food_entry.get())
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
    def bio_f5():
        backbutton(bio_frame,biof5_frame)
        def bio_f5_chap9():
            backbutton(biof5_frame,biof5c9_frame)
            def percentage_cover():
                backbutton(biof5c9_frame, percentage_cover_frame)
                def percentage_cover_calc():
                    number_of_squares_containing_a_species=int(number_of_squares_containing_a_species_entry.get())
                    total_number_of_squares = int(total_number_of_squares_entry.get())
                    if number_of_squares_containing_a_species<0 or total_number_of_squares<0:
                        messagebox.showerroe(title='Error',message='input cannot be negative')
                    else:
                        percentage_cover=number_of_squares_containing_a_species/total_number_of_squares*100    
                    result_label.config(text=f"{percentage_cover}")

                percentage_cover_label=tk.Label(percentage_cover_frame, text='percentage cover',  bg="#212129",fg="#08edff",font=("Helvetica",34))
                number_of_squares_containing_a_species_label=tk.Label(percentage_cover_frame, text='number of squares containing a species', bg="#212129",fg="#08edff",font=("Helvetica",24))    
                total_number_of_squares_label =tk.Label(percentage_cover_frame, text='total number of squares containing a species',  bg="#212129",fg="#08edff",font=("Helvetica",34))
                result_label=tk.Label(percentage_cover_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                number_of_squares_containing_a_species_entry=tk.Entry(percentage_cover_frame,font=("Helvetica", 16))
                total_number_of_squares_entry=tk.Entry(percentage_cover_frame, font=("Helvetica", 16))

                percentage_cover_back=tk.Button(percentage_cover_frame, text='Back',bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(percentage_cover_frame,biof4c9_frame,result_label))
                percentage_cover_back.grid(row=0, column=1,pady=10)
                calculate_button=tk.Button(percentage_cover_frame,tex='calculate',bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:percentage_cover_calc())
                calculate_button.grid(row=8,column=1,pady=10)

                percentage_cover_label.grid(row=0,column=1,pady=10)
                number_of_squares_containing_a_species_label.grid(row=1,column=0,pady=10)
                total_number_of_squares_label.grid(row=2,column=0,pady=10)
                number_of_squares_containing_a_species_entry.grid(row=1,column=2)
                total_number_of_squares_entry.grid(row=2,column=2)
                result_label.grid(row=3, column=1,pady=10)
            def population():
                backbutton(biof5c9_frame, population_frame)
                def population_calc():
                    first_catch_number=int(first_catch_entry.get())
                    second_catch_number=int(second_catch_number_entry.get())
                    marked_second_catch_number = int(marked_second_catch_number_entry.get())
                    if first_catch_number<0  :second_catch_number<0 or  marked_second_catch_number<0: 
                       messagebox.showerror(title='Error',message='input cannot be negative')
                    else:
                        population=first_catch_number*second_catch_number/marked_second_catch_number
                    result_label.config(text=f"{population}")

                population_label=tk.Label(population_frame, text='population',  bg="#212129",fg="#08edff",font=("Helvetica",34))
                first_catch_number_label=tk.Label(population_frame, text='first catch number',bg="#212129",fg="#08edff",font=("Helvetica",24))
                second_catch_number_label=tk.Label(population_frame, text='second catch number',bg="#212129",fg="#08edff",font=("Helvetica",24))
                marked_second_catch_number_label=tk.Label(population_frame, text='marked second catch number',bg="#212129",fg="#08edff",font=("Helvetica",24))
                result_label=tk.Label(population_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                first_catch_number_entry=tk.Entry(population_frame,font=("Helvetica", 16))
                second_catch_number_entry=tk.Entry(population_frame,font=("Helvetica", 16))
                marked_second_catch_number_entry=tk.Entry(population_frame,font=("Helvetica", 16))

                population_back=tk.Button(population_frame, text='Back',bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(population_frame,biof5c9_frame,result_label))
                population_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(population_frame,text="calculate",bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:population_calc())
                calculate_button.grid=tk.Button(row=8,column=1,pady=10)

                population_label.grid(row=0,column=1,pady=10)
                first_catch_number_label.grid(row=1,column=0,pady=10)
                second_catch_number_label.grid(row=2,column=0,pady=10)
                marked_second_catch_number_label.grid(row=3,column=0,pady=10)
                first_catch_number_entry.grid(row=1,column=2)
                second_catch_number_entry.grid(row=2,column=2)
                marked_second_catch_number_entry.grid(row=3,column=2)
                result_label.grid(row=3,column=1,pady=10)

            def transpiration_rate():
                backbutton(biof5c9_frame,transpiration_rate_frame)
                def transpiration_rate_calc():
                    distance_moved_by_air_bubble_from_x_to_y = int(distance_moved_by_air_bubble_from_x_to_y_entry.get())
                    time=int(time_entry.get())
                    if time<0 or distance_moved_by_air_bubble_from_x_to_y <0:
                        messagebox.showerror(title="Error", message="input cannot be negative")
                    else:
                        transpiration_rate = distance_moved_by_air_bubble_from_x_to_y/time 
                    result_label.config(text=f"{transpiration_rate}")

                transpiration_rate_label = tk.Label(transpiration_rate_frame,text="transpiration rate",bg="#212129",fg="#08edff",font=("Helvetica",34))
                distance_moved_by_air_bubble_from_x_to_y_label=tk.Label(transpiration_rate_frame,text="distance moved by air bubble from x to y",bg="#212129",fg="#08edff",font=("Helvetica",24))
                time_label=tk.Label(transpiration_rate_frame,text="time",bg="#212129",fg="#08edff",font=("Helvetica",24))     
                result_label=tk.Label(transpiration_rate_frame,text="",bg="#212129",fg="#FFFFFF", font=("Helvetica", 24))

                distance_moved_by_air_bubble_from_x_to_y_entry=tk.Entry(transpiration_rate_frame,font=("Helvetica",16))
                time_entry=tk.Entry(transpiration_rate_frame,font=("Helvetica",16))

                transpiration_rate_back=tk.Button(transpiration_rate_frame,text='Back',bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16), command=lambda:backbutton_delresult(population_frame,biof5c9_frame,result_label))
                transpiration_rate_back.grid(row=9,column=1,pady=10)
                calculate_button=tk.Button(transpiration_rate_frame,text='calculate',,bg="#1c6cc0", fg="#FFFFFF", font=("Helvetica", 16),command=lambda:transpiration_rate_calc())      
                calculate_button.grid(row=8,column=1,pady=10)

                transpiration_rate_label.grid(row=0,column=1,pady=10)
                distance_moved_by_air_bubble_from_x_to_y_label.grid(row=1,column=0,pady=10)
                time_label.grid(row=2,column=0,pady=10)
                distance_moved_by_air_bubble_from_x_to_y_entry.grid(row=1,column=2)
                time_entry.grid(row=2,column=2)
                result_label.grid(row=3,column=1,pady=10)


 